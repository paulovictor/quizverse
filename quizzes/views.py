from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.db.models import Sum
from .models import Theme, Quiz, Question, Answer, QuizAttempt, UserAnswer, Product
import random


def get_client_ip(request):
    """Helper para obter o IP do cliente"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def home(request):
    """Página inicial com categorias principais (temas sem parent)"""
    # Se for superuser, mostrar todos os temas (incluindo inativos)
    if request.user.is_authenticated and request.user.is_superuser:
        themes = Theme.objects.filter(parent__isnull=True).order_by('order', 'title')
    else:
        themes = Theme.objects.filter(parent__isnull=True, active=True).order_by('order', 'title')
    
    # Adicionar contagens para cada tema
    themes_with_info = []
    for theme in themes:
        # Superuser vê tudo, outros só os ativos
        if request.user.is_authenticated and request.user.is_superuser:
            subcategories_count = theme.subcategories.count()
            quiz_count = theme.quizzes.count()
        else:
            subcategories_count = theme.subcategories.filter(active=True).count()
            quiz_count = theme.quizzes.filter(active=True).count()
        
        themes_with_info.append({
            'theme': theme,
            'subcategories_count': subcategories_count,
            'quiz_count': quiz_count,
            'total_count': subcategories_count + quiz_count
        })
    
    context = {
        'themes_with_info': themes_with_info,
        'is_root': True,
    }
    return render(request, 'quizzes/home.html', context)


def theme_detail(request, theme_slug):
    """Lista subcategorias e quizzes de um tema"""
    # Superuser pode acessar temas inativos
    if request.user.is_authenticated and request.user.is_superuser:
        theme = get_object_or_404(Theme, slug=theme_slug)
        subcategories = theme.subcategories.all().order_by('order', 'title')
        quizzes = theme.quizzes.all().order_by('order', 'title')
    else:
        theme = get_object_or_404(Theme, slug=theme_slug, active=True)
        subcategories = theme.subcategories.filter(active=True).order_by('order', 'title')
        quizzes = theme.quizzes.filter(active=True).order_by('order', 'title')
    
    # Adicionar contagens para subcategorias
    subcategories_with_info = []
    for subcat in subcategories:
        if request.user.is_authenticated and request.user.is_superuser:
            sub_count = subcat.subcategories.count()
            quiz_count = subcat.quizzes.count()
        else:
            sub_count = subcat.subcategories.filter(active=True).count()
            quiz_count = subcat.quizzes.filter(active=True).count()
        
        subcategories_with_info.append({
            'theme': subcat,
            'subcategories_count': sub_count,
            'quiz_count': quiz_count,
            'total_count': sub_count + quiz_count
        })
    
    # Buscar produtos relacionados ao tema
    products = Product.objects.filter(
        theme=theme,
        active=True
    ).order_by('order', 'title')[:3]  # Máximo 3 produtos
    
    # Gerar breadcrumb
    breadcrumb = theme.get_breadcrumb()
    
    context = {
        'theme': theme,
        'subcategories': subcategories_with_info,
        'quizzes': quizzes,
        'products': products,
        'breadcrumb': breadcrumb,
    }
    return render(request, 'quizzes/theme_detail.html', context)


def quiz_detail(request, theme_slug, quiz_slug):
    """Página de detalhes do quiz antes de iniciar"""
    # Superuser pode acessar temas e quizzes inativos
    if request.user.is_authenticated and request.user.is_superuser:
        theme = get_object_or_404(Theme, slug=theme_slug)
        quiz = get_object_or_404(Quiz, theme=theme, slug=quiz_slug)
    else:
        theme = get_object_or_404(Theme, slug=theme_slug, active=True)
        quiz = get_object_or_404(Quiz, theme=theme, slug=quiz_slug, active=True)
    
    # Buscar tentativas anteriores do usuário
    previous_attempts = None
    if request.user.is_authenticated:
        previous_attempts = QuizAttempt.objects.filter(
            user=request.user,
            quiz=quiz,
            completed_at__isnull=False
        ).order_by('-completed_at')[:5]
    
    # Gerar breadcrumb
    breadcrumb = theme.get_breadcrumb()
    
    context = {
        'theme': theme,
        'quiz': quiz,
        'total_questions': quiz.get_total_questions(),
        'total_points': quiz.get_total_points(),
        'previous_attempts': previous_attempts,
        'breadcrumb': breadcrumb,
    }
    return render(request, 'quizzes/quiz_detail.html', context)


@require_POST
def quiz_start(request, theme_slug, quiz_slug):
    """Inicia uma nova tentativa de quiz"""
    # Superuser pode iniciar quizzes inativos
    if request.user.is_authenticated and request.user.is_superuser:
        theme = get_object_or_404(Theme, slug=theme_slug)
        quiz = get_object_or_404(Quiz, theme=theme, slug=quiz_slug)
    else:
        theme = get_object_or_404(Theme, slug=theme_slug, active=True)
        quiz = get_object_or_404(Quiz, theme=theme, slug=quiz_slug, active=True)
    
    # Verificar se há perguntas
    if quiz.get_total_questions() == 0:
        messages.error(request, 'Este quiz ainda não possui perguntas.')
        return redirect('quizzes:quiz_detail', theme_slug=theme_slug, quiz_slug=quiz_slug)
    
    # Criar nova tentativa
    attempt = QuizAttempt.objects.create(
        user=request.user if request.user.is_authenticated else None,
        quiz=quiz,
        session_key=request.session.session_key or '',
        ip_address=get_client_ip(request),
    )
    
    # Garantir que a sessão existe para usuários anônimos
    if not request.session.session_key:
        request.session.create()
        attempt.session_key = request.session.session_key
        attempt.save()
    
    # Randomizar perguntas
    attempt.initialize_question_order()
    
    # Redirecionar para a primeira pergunta
    return redirect('quizzes:quiz_play', attempt_id=attempt.id)


def quiz_play(request, attempt_id):
    """Página para jogar o quiz"""
    attempt = get_object_or_404(QuizAttempt, id=attempt_id)
    
    # Verificar permissão (usuário logado ou mesma sessão)
    if request.user.is_authenticated:
        if attempt.user and attempt.user != request.user:
            messages.error(request, 'Você não tem permissão para acessar esta tentativa.')
            return redirect('quizzes:theme_detail', theme_slug=attempt.quiz.theme.slug)
    else:
        if attempt.session_key != request.session.session_key:
            messages.error(request, 'Você não tem permissão para acessar esta tentativa.')
            return redirect('quizzes:theme_detail', theme_slug=attempt.quiz.theme.slug)
    
    # Se já foi completado, redirecionar para resultado
    if attempt.is_completed():
        return redirect('quizzes:quiz_result', attempt_id=attempt.id)
    
    # Pegar perguntas na ordem randomizada
    questions = attempt.get_ordered_questions()
    
    # Pegar respostas já dadas
    answered_question_ids = set(
        str(qid) for qid in attempt.user_answers.values_list('question_id', flat=True)
    )
    
    # Encontrar próxima pergunta não respondida
    current_question = None
    current_index = 0
    for idx, question in enumerate(questions):
        if str(question.id) not in answered_question_ids:
            current_question = question
            current_index = idx
            break
    
    # Se todas foram respondidas, redirecionar para finalizar
    if current_question is None:
        return redirect('quizzes:quiz_finish', attempt_id=attempt.id)
    
    # Randomizar alternativas
    answers = list(current_question.answers.all())
    random.shuffle(answers)
    
    # Gerar breadcrumb
    breadcrumb = attempt.quiz.theme.get_breadcrumb()
    
    context = {
        'attempt': attempt,
        'quiz': attempt.quiz,
        'theme': attempt.quiz.theme,
        'question': current_question,
        'answers': answers,
        'current_index': current_index + 1,
        'total_questions': len(questions),
        'progress_percentage': (current_index / len(questions)) * 100,
        'breadcrumb': breadcrumb,
    }
    return render(request, 'quizzes/quiz_play.html', context)


@require_POST
def quiz_answer(request, attempt_id):
    """Processa a resposta de uma pergunta"""
    attempt = get_object_or_404(QuizAttempt, id=attempt_id)
    
    # Verificar permissão
    if request.user.is_authenticated:
        if attempt.user and attempt.user != request.user:
            return JsonResponse({'error': 'Sem permissão'}, status=403)
    else:
        if attempt.session_key != request.session.session_key:
            return JsonResponse({'error': 'Sem permissão'}, status=403)
    
    # Verificar se já foi completado
    if attempt.is_completed():
        return JsonResponse({'error': 'Quiz já finalizado'}, status=400)
    
    # Pegar dados do POST
    question_id = request.POST.get('question_id')
    answer_id = request.POST.get('answer_id')
    
    if not question_id or not answer_id:
        return JsonResponse({'error': 'Dados inválidos'}, status=400)
    
    # Validar pergunta e resposta
    question = get_object_or_404(Question, id=question_id, quiz=attempt.quiz)
    answer = get_object_or_404(Answer, id=answer_id, question=question)
    
    # Criar ou atualizar resposta do usuário
    user_answer, created = UserAnswer.objects.get_or_create(
        attempt=attempt,
        question=question,
        defaults={'selected_answer': answer}
    )
    
    if not created:
        # Atualizar se já existia
        user_answer.selected_answer = answer
        user_answer.save()
    
    return JsonResponse({
        'success': True,
        'is_correct': user_answer.is_correct,
        'points_earned': user_answer.points_earned,
    })


def quiz_finish(request, attempt_id):
    """Finaliza o quiz e calcula a pontuação"""
    attempt = get_object_or_404(QuizAttempt, id=attempt_id)
    
    # Verificar permissão
    if request.user.is_authenticated:
        if attempt.user and attempt.user != request.user:
            messages.error(request, 'Você não tem permissão para acessar esta tentativa.')
            return redirect('quizzes:theme_detail', theme_slug=attempt.quiz.theme.slug)
    else:
        if attempt.session_key != request.session.session_key:
            messages.error(request, 'Você não tem permissão para acessar esta tentativa.')
            return redirect('quizzes:theme_detail', theme_slug=attempt.quiz.theme.slug)
    
    # Verificar se todas as perguntas foram respondidas
    questions = attempt.get_ordered_questions()
    answered_count = attempt.user_answers.count()
    
    if answered_count < len(questions):
        messages.warning(request, f'Você respondeu apenas {answered_count} de {len(questions)} perguntas.')
    
    # Calcular pontuação se ainda não foi finalizado
    if not attempt.is_completed():
        total_score = attempt.user_answers.aggregate(
            total=Sum('points_earned')
        )['total'] or 0
        
        attempt.score = total_score
        attempt.completed_at = timezone.now()
        attempt.save()
    
    return redirect('quizzes:quiz_result', attempt_id=attempt.id)


def quiz_result(request, attempt_id):
    """Exibe o resultado do quiz"""
    attempt = get_object_or_404(QuizAttempt, id=attempt_id)
    
    # Verificar permissão
    if request.user.is_authenticated:
        if attempt.user and attempt.user != request.user:
            messages.error(request, 'Você não tem permissão para acessar esta tentativa.')
            return redirect('quizzes:theme_detail', theme_slug=attempt.quiz.theme.slug)
    else:
        if attempt.session_key != request.session.session_key:
            messages.error(request, 'Você não tem permissão para acessar esta tentativa.')
            return redirect('quizzes:theme_detail', theme_slug=attempt.quiz.theme.slug)
    
    # Pegar todas as respostas com perguntas na ordem
    questions = attempt.get_ordered_questions()
    user_answers_dict = {
        str(ua.question.id): ua 
        for ua in attempt.user_answers.select_related('question', 'selected_answer').all()
    }
    
    # Montar lista de resultados
    results = []
    for question in questions:
        user_answer = user_answers_dict.get(str(question.id))
        correct_answer = question.get_correct_answer()
        
        results.append({
            'question': question,
            'user_answer': user_answer,
            'correct_answer': correct_answer,
            'all_answers': question.answers.all(),
        })
    
    # Buscar produtos relacionados ao tema
    products = Product.objects.filter(
        theme=attempt.quiz.theme,
        active=True
    ).order_by('order', 'title')[:3]  # Máximo 3 produtos
    
    # Gerar breadcrumb
    breadcrumb = attempt.quiz.theme.get_breadcrumb()
    
    context = {
        'attempt': attempt,
        'quiz': attempt.quiz,
        'theme': attempt.quiz.theme,
        'results': results,
        'percentage': attempt.get_score_percentage(),
        'show_login_prompt': not request.user.is_authenticated and not attempt.user,
        'products': products,
        'breadcrumb': breadcrumb,
    }
    return render(request, 'quizzes/quiz_result.html', context)


@login_required
def claim_attempt(request, attempt_id):
    """Associa uma tentativa anônima ao usuário logado"""
    attempt = get_object_or_404(QuizAttempt, id=attempt_id)
    
    # Verificar se é uma tentativa anônima
    if attempt.user is not None:
        # Já está associada a um usuário, apenas mostrar o resultado
        if attempt.user == request.user:
            messages.info(request, 'Este resultado já está salvo na sua conta.')
        else:
            messages.error(request, 'Esta tentativa pertence a outro usuário.')
        return redirect('quizzes:quiz_result', attempt_id=attempt.id)
    
    # Associar ao usuário
    # A sessão muda quando o usuário faz login por segurança,
    # então não podemos verificar session_key aqui
    attempt.user = request.user
    attempt.save()
    
    messages.success(request, '🎉 Resultado salvo com sucesso na sua conta!')
    return redirect('quizzes:quiz_result', attempt_id=attempt.id)
