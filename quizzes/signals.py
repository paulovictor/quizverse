"""
Signals para o app quizzes
"""
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import QuizAttempt


def get_client_ip(request):
    """Helper para obter o IP do cliente"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@receiver(user_logged_in)
def associate_anonymous_attempts(sender, request, user, **kwargs):
    """
    Associa automaticamente tentativas anônimas ao usuário após login/signup.
    Busca por session_key E por IP address (caso a sessão tenha sido regenerada).
    """
    from django.contrib import messages
    from django.db.models import Q
    from django.utils import timezone
    from datetime import timedelta
    
    session_key = request.session.session_key
    ip_address = get_client_ip(request)
    
    # Buscar tentativas dos últimos 24 horas (para evitar associar tentativas muito antigas)
    last_24h = timezone.now() - timedelta(hours=24)
    
    # Construir query: tentativas anônimas da sessão OU do mesmo IP nas últimas 24h
    query = Q(user__isnull=True, started_at__gte=last_24h)
    
    if session_key:
        query &= Q(session_key=session_key) | Q(ip_address=ip_address)
    else:
        query &= Q(ip_address=ip_address)
    
    # Encontrar tentativas anônimas
    anonymous_attempts = QuizAttempt.objects.filter(query)
    
    # Associar ao usuário
    count = anonymous_attempts.update(user=user)
    
    if count > 0:
        # Adicionar mensagem de sucesso
        if count == 1:
            messages.success(request, '🎉 Seu resultado foi salvo na sua conta!')
        else:
            messages.success(request, f'🎉 {count} resultados foram salvos na sua conta!')

