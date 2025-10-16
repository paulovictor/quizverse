from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django_ratelimit.decorators import ratelimit
from .models import Theme, Quiz, Question, Answer, QuizAttempt, UserAnswer, Product
from .decorators import validate_attempt_access
from .services import check_and_award_badges
import random


def get_user_country(request):
    """Helper para obter o país preferido do usuário"""
    # Primeiro verifica na sessão
    country = request.session.get('country')
    if country:
        return country
    
    # Se não tiver na sessão, usar pt-BR como padrão
    return 'pt-BR'


def country_to_language(country_code):
    """Converte código de país para código de idioma para traduções"""
    # Mapeamento de país para idioma
    country_to_lang_map = {
        'pt-BR': 'pt',
        'pt-PT': 'pt',
        'en-US': 'en',
        'en-CA': 'en',
        'en-GB': 'en',
        'en-IN': 'en',
        'en-PH': 'en',
        'en-AU': 'en',
        'en-NZ': 'en',
        'es-MX': 'es',
        'es-ES': 'es',
        'es-AR': 'es',
        'es-CO': 'es',
        'de-DE': 'de',
        'fr-FR': 'fr',
        'it-IT': 'it',
        'nl-NL': 'nl',
        'sv-SE': 'sv',
        'no-NO': 'no',
        'pl-PL': 'pl',
        'id-ID': 'id',
        'ja-JP': 'ja',
        'ko-KR': 'ko',
        'th-TH': 'th',
        'vi-VN': 'vi',
    }
    return country_to_lang_map.get(country_code, 'pt')


def get_country_context(request):
    """Helper para adicionar contexto de país ao template"""
    user_country = get_user_country(request)
    user_language = country_to_language(user_country)
    
    # Estatísticas de países para o footer - usando underscore para compatibilidade com templates
    country_stats = {}
    for country_code, country_name in Theme.COUNTRY_CHOICES:
        quiz_count = Quiz.objects.filter(active=True, country=country_code).count()
        # Substituir hífen por underscore para funcionar nos templates
        safe_key = country_code.replace('-', '_')
        country_stats[safe_key] = quiz_count
    
    return {
        'current_country': user_country,
        'current_language': user_language,
        'country_stats': country_stats,
    }


@csrf_exempt
@ratelimit(key='ip', rate='20/h', method='POST', block=True)
def set_country(request):
    """View para trocar o país do usuário (não requer CSRF pois é operação segura)"""
    if request.method == 'POST':
        country = request.POST.get('country', 'pt-BR')
        
        # Validar se é um país suportado
        supported_countries = [code for code, name in Theme.COUNTRY_CHOICES]
        if country in supported_countries:
            # Garantir que a sessão seja criada (importante para modo incógnito/primeira visita)
            if not request.session.session_key:
                request.session.create()
            
            # Salvar o país na sessão
            request.session['country'] = country
            
            # Forçar modificação da sessão para garantir que seja salva
            request.session.modified = True
            
            return JsonResponse({'success': True, 'country': country})
        
        return JsonResponse({'success': False, 'error': 'País não suportado'}, status=400)
    
    return JsonResponse({'success': False, 'error': 'Método não permitido'}, status=405)


def get_client_ip(request):
    """Helper para obter o IP do cliente"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_all_descendant_quizzes(theme, is_superuser=False):
    """Retorna todos os quizzes descendentes de um tema (recursivo)"""
    quizzes = []
    
    # Quizzes diretos deste tema
    if is_superuser:
        direct_quizzes = list(theme.quizzes.all())
    else:
        direct_quizzes = list(theme.quizzes.filter(active=True))
    
    quizzes.extend(direct_quizzes)
    
    # Quizzes dos filhos (recursivo)
    if is_superuser:
        children = theme.subcategories.all()
    else:
        children = theme.subcategories.filter(active=True)
    
    for child in children:
        quizzes.extend(get_all_descendant_quizzes(child, is_superuser))
    
    return quizzes


@ensure_csrf_cookie
def home(request):
    """Página inicial com categorias principais (temas sem parent)"""
    # Obter país do usuário
    user_country = get_user_country(request)
    
    # Se for superuser, mostrar todos os temas (incluindo inativos)
    if request.user.is_authenticated and request.user.is_superuser:
        themes = Theme.objects.filter(
            parent__isnull=True, country=user_country
        ).prefetch_related('subcategories', 'quizzes').order_by('order', 'title')
        all_quizzes = Quiz.objects.filter(country=user_country).select_related('theme')
        all_themes = Theme.objects.filter(country=user_country)
    else:
        themes = Theme.objects.filter(
            parent__isnull=True, active=True, country=user_country
        ).prefetch_related('subcategories', 'quizzes').order_by('order', 'title')
        all_quizzes = Quiz.objects.filter(active=True, country=user_country).select_related('theme')
        all_themes = Theme.objects.filter(active=True, country=user_country)
    
    # Adicionar contagens para cada tema
    categories = []
    for theme in themes:
        is_superuser = request.user.is_authenticated and request.user.is_superuser
        
        # Buscar todos os quizzes descendentes (recursivo)
        all_theme_quizzes = get_all_descendant_quizzes(theme, is_superuser)
        total_quizzes = len(all_theme_quizzes)
        
        # Calcular progresso do usuário
        completed_quizzes = 0
        if request.user.is_authenticated:
            # Quizzes que o usuário completou (distinct)
            quiz_ids = [q.id for q in all_theme_quizzes]
            completed_quizzes = QuizAttempt.objects.filter(
                user=request.user,
                quiz_id__in=quiz_ids,
                completed_at__isnull=False
            ).values('quiz_id').distinct().count()
        
        # Contagem de subcategorias diretas (para exibição)
        if is_superuser:
            subcategories_count = theme.subcategories.filter(country=user_country).count()
        else:
            subcategories_count = theme.subcategories.filter(active=True, country=user_country).count()
        
        categories.append({
            'theme': theme,
            'subcategories_count': subcategories_count,
            'quiz_count': total_quizzes,
            'completed_quizzes': completed_quizzes,
            'total_count': subcategories_count + total_quizzes
        })
    
    # Estatísticas globais
    total_themes = all_themes.count()
    total_quizzes = all_quizzes.count()
    total_questions = Question.objects.filter(quiz__in=all_quizzes).count()
    
    context = {
        'categories': categories,
        'total_themes': total_themes,
        'total_quizzes': total_quizzes,
        'total_questions': total_questions,
        'is_root': True,
        **get_country_context(request),
    }
    return render(request, 'quizzes/home.html', context)


def theme_detail(request, theme_slug):
    """Lista subcategorias e quizzes de um tema"""
    # Obter idioma do usuário
    user_country = get_user_country(request)
    
    # Superuser pode acessar temas inativos
    if request.user.is_authenticated and request.user.is_superuser:
        theme = get_object_or_404(Theme.objects.select_related('parent'), slug=theme_slug)
        subcategories = theme.subcategories.filter(
            country=user_country
        ).prefetch_related('subcategories', 'quizzes').order_by('order', 'title')
        quizzes = theme.quizzes.filter(country=user_country).select_related('quiz_group').prefetch_related(
            'quiz_group__available_badges__badge'
        ).order_by('quiz_group__order', 'order', 'title')
    else:
        theme = get_object_or_404(Theme.objects.select_related('parent'), slug=theme_slug, active=True)
        subcategories = theme.subcategories.filter(
            active=True, country=user_country
        ).prefetch_related('subcategories', 'quizzes').order_by('order', 'title')
        quizzes = theme.quizzes.filter(active=True, country=user_country).select_related('quiz_group').prefetch_related(
            'quiz_group__available_badges__badge'
        ).order_by('quiz_group__order', 'order', 'title')
    
    # Adicionar contagens para subcategorias
    subcategories_with_info = []
    for subcat in subcategories:
        if request.user.is_authenticated and request.user.is_superuser:
            sub_count = subcat.subcategories.filter(country=user_country).count()
            quiz_count = subcat.quizzes.filter(country=user_country).count()
        else:
            sub_count = subcat.subcategories.filter(active=True, country=user_country).count()
            quiz_count = subcat.quizzes.filter(active=True, country=user_country).count()
        
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
        **get_country_context(request),
    }
    return render(request, 'quizzes/theme_detail.html', context)


def quiz_detail(request, theme_slug, quiz_slug):
    """Página de detalhes do quiz antes de iniciar"""
    # Superuser pode acessar temas e quizzes inativos
    if request.user.is_authenticated and request.user.is_superuser:
        theme = get_object_or_404(Theme.objects.select_related('parent'), slug=theme_slug)
        quiz = get_object_or_404(
            Quiz.objects.select_related('theme').prefetch_related('questions'),
            theme=theme, slug=quiz_slug
        )
    else:
        theme = get_object_or_404(Theme.objects.select_related('parent'), slug=theme_slug, active=True)
        quiz = get_object_or_404(
            Quiz.objects.select_related('theme').prefetch_related('questions'),
            theme=theme, slug=quiz_slug, active=True
        )
    
    # Buscar tentativas anteriores do usuário
    user_attempts = None
    stats = None
    if request.user.is_authenticated:
        # Buscar todas as tentativas (completadas e não completadas)
        # Ordenar: completadas por data desc, depois não completadas por data desc
        from django.db.models import Case, When, Value, IntegerField
        
        attempts = QuizAttempt.objects.filter(
            user=request.user,
            quiz=quiz,
        ).annotate(
            is_completed=Case(
                When(completed_at__isnull=False, then=Value(1)),
                default=Value(0),
                output_field=IntegerField(),
            )
        ).order_by('-is_completed', '-started_at')[:10]
        
        # Calcular porcentagem para cada tentativa e converter para lista
        user_attempts = []
        for attempt in attempts:
            # Calcular porcentagem
            if attempt.max_score > 0:
                percentage = (attempt.score / attempt.max_score) * 100
            else:
                percentage = 0
            
            # Adicionar porcentagem e total_score como atributos temporários
            attempt.percentage = percentage
            attempt.total_score = attempt.score  # Alias para template
            
            # Adicionar duração formatada
            attempt.duration_formatted = attempt.get_duration_formatted()
            
            # Para tentativas não completadas, contar quantas questões já foram respondidas
            if attempt.completed_at is None:
                attempt.answered_questions = attempt.user_answers.count()
                attempt.remaining_questions = attempt.max_score - attempt.answered_questions
                # Calcular porcentagem de progresso
                if attempt.max_score > 0:
                    attempt.progress_percentage = int((attempt.answered_questions / attempt.max_score) * 100)
                else:
                    attempt.progress_percentage = 0
            
            user_attempts.append(attempt)
        
        # Calcular estatísticas (apenas tentativas completadas)
        completed_attempts = [a for a in user_attempts if a.completed_at is not None]
        if completed_attempts:
            total_attempts = len(completed_attempts)
            best_percentage = max(attempt.percentage for attempt in completed_attempts)
            avg_percentage = sum(attempt.percentage for attempt in completed_attempts) / total_attempts
            
            stats = {
                'total_attempts': total_attempts,
                'best_percentage': best_percentage,
                'avg_percentage': avg_percentage,
            }
    
    # Gerar breadcrumb
    breadcrumb = theme.get_breadcrumb()
    
    context = {
        'theme': theme,
        'quiz': quiz,
        'total_questions': quiz.get_questions_per_attempt(),  # Número de questões por tentativa
        'total_questions_available': quiz.get_total_questions(),  # Total cadastrado
        'user_attempts': user_attempts,
        'stats': stats,
        'breadcrumb': breadcrumb,
        **get_country_context(request),
    }
    return render(request, 'quizzes/quiz_detail.html', context)


@require_POST
@ratelimit(key='ip', rate='10/m', method='POST', block=True)
def quiz_start(request, theme_slug, quiz_slug):
    """Inicia uma nova tentativa de quiz"""
    # Superuser pode iniciar quizzes inativos
    if request.user.is_authenticated and request.user.is_superuser:
        theme = get_object_or_404(Theme.objects.select_related('parent'), slug=theme_slug)
        quiz = get_object_or_404(
            Quiz.objects.select_related('theme').prefetch_related('questions'),
            theme=theme, slug=quiz_slug
        )
    else:
        theme = get_object_or_404(Theme.objects.select_related('parent'), slug=theme_slug, active=True)
        quiz = get_object_or_404(
            Quiz.objects.select_related('theme').prefetch_related('questions'),
            theme=theme, slug=quiz_slug, active=True
        )
    
    # Verificar se há questões
    if quiz.get_total_questions() == 0:
        messages.error(request, 'Este quiz ainda não possui questões.')
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
    
    # Randomizar questões
    attempt.initialize_question_order()
    
    # Redirecionar para a primeira questão
    return redirect('quizzes:quiz_play', attempt_id=attempt.id)


@validate_attempt_access()
def quiz_play(request, attempt_id, attempt=None):
    """Página para jogar o quiz"""
    # attempt is now passed by the decorator
    
    # Se já foi completado, redirecionar para resultado
    if attempt.is_completed():
        return redirect('quizzes:quiz_result', attempt_id=attempt.id)
    
    # Pegar questões na ordem randomizada
    questions = attempt.get_ordered_questions()
    
    # Pegar respostas já dadas
    answered_question_ids = set(
        str(qid) for qid in attempt.user_answers.values_list('question_id', flat=True)
    )
    
    # Encontrar próxima questão não respondida
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
        **get_country_context(request),
    }
    return render(request, 'quizzes/quiz_play.html', context)


@require_POST
@ratelimit(key='ip', rate='30/m', method='POST', block=True)
@validate_attempt_access(redirect_on_error=False)
def quiz_answer(request, attempt_id, attempt=None):
    """Processa a resposta de uma questão"""
    # attempt is now passed by the decorator
    
    # Verificar se já foi completado
    if attempt.is_completed():
        return JsonResponse({'error': 'Quiz já finalizado'}, status=400)
    
    # Pegar dados do POST
    question_id = request.POST.get('question_id')
    answer_id = request.POST.get('answer_id')
    
    if not question_id or not answer_id:
        return JsonResponse({'error': 'Dados inválidos'}, status=400)
    
    # Validar questão e resposta
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
    })


@validate_attempt_access()
def quiz_finish(request, attempt_id, attempt=None):
    """Finaliza o quiz e calcula a pontuação"""
    # attempt is now passed by the decorator
    
    # Verificar se todas as questões foram respondidas
    questions = attempt.get_ordered_questions()
    answered_count = attempt.user_answers.count()
    
    if answered_count < len(questions):
        messages.warning(request, f'Você respondeu apenas {answered_count} de {len(questions)} questões.')
    
    # Calcular pontuação se ainda não foi finalizado
    if not attempt.is_completed():
        total_score = attempt.user_answers.filter(is_correct=True).count()
        
        attempt.score = total_score
        attempt.completed_at = timezone.now()
        attempt.save()
    
    return redirect('quizzes:quiz_result', attempt_id=attempt.id)


@validate_attempt_access()
def quiz_result(request, attempt_id, attempt=None):
    """Exibe o resultado do quiz"""
    # attempt is now passed by the decorator
    
    # Pegar todas as respostas com questões na ordem
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
    ).order_by('order', 'title')[:6]  # Máximo 6 produtos
    
    # Gerar breadcrumb
    breadcrumb = attempt.quiz.theme.get_breadcrumb()
    
    # Determinar categoria de performance
    percentage = attempt.get_score_percentage()
    if percentage == 100:
        performance_level = 'excellent'
        performance_message = 'Perfeito!'
        performance_icon = '🎉'
    elif percentage >= 80:
        performance_level = 'excellent'
        performance_message = 'Excelente!'
        performance_icon = '🎉'
    elif percentage >= 50:
        performance_level = 'good'
        performance_message = 'Bom trabalho!'
        performance_icon = '👍'
    elif percentage >= 30:
        performance_level = 'poor'
        performance_message = 'Continue praticando!'
        performance_icon = '💪'
    else:
        performance_level = 'very-poor'
        performance_message = 'Tente novamente!'
        performance_icon = '📚'
    
    # Calcular ranking do usuário neste quiz
    # Para usuários autenticados: considerar apenas a melhor tentativa de cada usuário
    # Para usuários não autenticados: considerar cada tentativa como usuário diferente
    
    from django.db.models import Max
    
    if attempt.user:
        # Usuário autenticado: pegar a melhor pontuação de cada usuário (exceto o atual)
        best_scores_other_users = QuizAttempt.objects.filter(
            quiz=attempt.quiz,
            completed_at__isnull=False,
            user__isnull=False
        ).exclude(user=attempt.user).values('user').annotate(
            best_score=Max('score')
        ).values_list('best_score', flat=True)
        
        # Converter para lista e adicionar a pontuação atual
        all_scores = list(best_scores_other_users) + [attempt.score]
        
        # Adicionar tentativas de usuários não autenticados
        anonymous_scores = QuizAttempt.objects.filter(
            quiz=attempt.quiz,
            completed_at__isnull=False,
            user__isnull=True
        ).values_list('score', flat=True)
        
        all_scores.extend(anonymous_scores)
    else:
        # Usuário não autenticado: comparar com todas as tentativas
        all_scores = list(QuizAttempt.objects.filter(
            quiz=attempt.quiz,
            completed_at__isnull=False
        ).values_list('score', flat=True))
    
    total_attempts = len(all_scores)
    
    # Contar quantos scores são maiores que o atual
    better_scores = sum(1 for score in all_scores if score > attempt.score)
    
    # Posição do usuário (1 = primeiro lugar)
    user_rank = better_scores + 1
    
    # Calcular percentual de usuários que ele superou
    if total_attempts > 1:
        users_beaten_percentage = round(((total_attempts - user_rank) / (total_attempts - 1)) * 100, 1)
    else:
        users_beaten_percentage = 0
    
    # Verificar e conceder badges (se usuário autenticado)
    new_badges = []
    if attempt.user and attempt.is_completed():
        new_badges = check_and_award_badges(attempt)
    
    context = {
        'attempt': attempt,
        'quiz': attempt.quiz,
        'theme': attempt.quiz.theme,
        'results': results,
        'percentage': percentage,
        'performance_level': performance_level,
        'performance_message': performance_message,
        'performance_icon': performance_icon,
        'total_score': attempt.score,
        'total_questions': attempt.max_score,
        'show_login_prompt': not request.user.is_authenticated and not attempt.user,
        'products': products,
        'breadcrumb': breadcrumb,
        'user_rank': user_rank,
        'total_attempts': total_attempts,
        'users_beaten_percentage': users_beaten_percentage,
        'new_badges': new_badges,
        'show_badge_celebration': len(new_badges) > 0,
        **get_country_context(request),
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


@login_required
def user_profile(request):
    """Página de perfil do usuário com suas estatísticas e histórico de quizzes"""
    user = request.user
    
    # Buscar todas as tentativas do usuário (completas) - otimizado com select_related
    attempts = QuizAttempt.objects.filter(
        user=user, 
        completed_at__isnull=False
    ).select_related('quiz', 'quiz__theme', 'quiz__theme__parent').order_by('-completed_at')
    
    # Calcular estatísticas gerais
    total_attempts = attempts.count()
    
    if total_attempts > 0:
        # Taxa de acerto média
        total_correct = sum(attempt.score for attempt in attempts)
        total_possible = sum(attempt.max_score for attempt in attempts)
        accuracy_rate = int((total_correct / total_possible * 100)) if total_possible > 0 else 0
        
        # Quizzes perfeitos (100% de acerto)
        perfect_quizzes = sum(1 for attempt in attempts if attempt.score == attempt.max_score and attempt.max_score > 0)
    else:
        accuracy_rate = 0
        perfect_quizzes = 0
    
    # Filtro por categoria
    category_filter = request.GET.get('category', 'all')
    
    if category_filter != 'all':
        # Filtrar por tema e seus sub-temas
        try:
            parent_theme = Theme.objects.get(slug=category_filter)
            # Pegar o tema e todos os seus descendentes
            theme_ids = [parent_theme.id]
            # Adicionar todos os filhos diretos
            children = Theme.objects.filter(parent=parent_theme)
            theme_ids.extend(children.values_list('id', flat=True))
            # Adicionar netos (se houver)
            for child in children:
                grandchildren = Theme.objects.filter(parent=child)
                theme_ids.extend(grandchildren.values_list('id', flat=True))
            
            attempts = attempts.filter(quiz__theme__id__in=theme_ids)
        except Theme.DoesNotExist:
            pass
    
    # Organizar tentativas com dados adicionais
    attempts_data = []
    for attempt in attempts:
        accuracy = int((attempt.score / attempt.max_score * 100)) if attempt.max_score > 0 else 0
        
        # Determinar o badge/mensagem baseado na performance
        if accuracy == 100:
            badge = 'Perfeito! 🎉'
            badge_class = 'perfect'
        elif accuracy >= 80:
            badge = 'Muito Bom!'
            badge_class = 'great'
        elif accuracy >= 60:
            badge = 'Bom!'
            badge_class = 'good'
        else:
            badge = 'Continue Tentando!'
            badge_class = 'try-again'
        
        attempts_data.append({
            'attempt': attempt,
            'accuracy': accuracy,
            'badge': badge,
            'badge_class': badge_class,
        })
    
    # Buscar temas raiz (sem parent) únicos das tentativas para o filtro - otimizado
    themes = Theme.objects.filter(
        quizzes__attempts__user=user,
        quizzes__attempts__completed_at__isnull=False,
        parent__isnull=True
    ).prefetch_related('quizzes').distinct().order_by('order', 'title')
    
    context = {
        'user': user,
        'total_attempts': total_attempts,
        'accuracy_rate': accuracy_rate,
        'perfect_quizzes': perfect_quizzes,
        'attempts_data': attempts_data,
        'themes': themes,
        'category_filter': category_filter,
        **get_country_context(request),
    }
    
    return render(request, 'quizzes/user_profile.html', context)
