"""
Serviços para gerenciamento de badges
"""
from django.db import transaction
from decimal import Decimal
from .models import Badge, QuizGroupBadge, UserBadge


def check_and_award_badges(quiz_attempt):
    """
    Verifica e concede badges após completar um quiz.
    
    Args:
        quiz_attempt: QuizAttempt completo
    
    Returns:
        list: Lista de UserBadge recém conquistadas
    """
    if not quiz_attempt.is_completed() or not quiz_attempt.user:
        return []
    
    user = quiz_attempt.user
    quiz = quiz_attempt.quiz
    
    # Se o quiz não tem grupo, não pode ter badges
    if not quiz.quiz_group:
        return []
    
    quiz_group = quiz.quiz_group
    
    # Query simples: badges disponíveis para o grupo
    available_badges = Badge.objects.filter(
        quiz_groups__quiz_group=quiz_group,
        quiz_groups__active=True,
        active=True
    ).distinct()
    
    # Query simples: badges que o usuário já tem nesse grupo
    existing_badge_ids = set(
        UserBadge.objects.filter(
            user=user,
            quiz_group=quiz_group
        ).values_list('badge_id', flat=True)
    )
    
    newly_earned = []
    
    for badge in available_badges:
        # Já tem? Pula
        if badge.pk in existing_badge_ids:
            continue
        
        # Verifica critérios
        if badge_criteria_met(quiz_attempt, badge):
            with transaction.atomic():
                user_badge = UserBadge.objects.create(
                    user=user,
                    badge=badge,
                    quiz_group=quiz_group,
                    quiz_attempt=quiz_attempt,
                    score_percentage=quiz_attempt.get_score_percentage(),
                    completion_time_seconds=quiz_attempt.get_duration()
                )
                newly_earned.append(user_badge)
    
    return newly_earned


def badge_criteria_met(quiz_attempt, badge):
    """
    Verifica se o quiz_attempt atende aos critérios da badge.
    
    Args:
        quiz_attempt: QuizAttempt a ser verificado
        badge: Badge com os critérios
    
    Returns:
        bool: True se atende aos critérios
    """
    percentage = Decimal(str(quiz_attempt.get_score_percentage()))
    
    if badge.rule_type == 'percentage':
        return percentage >= badge.min_percentage
    
    elif badge.rule_type == 'percentage_time':
        duration = quiz_attempt.get_duration()
        return percentage >= badge.min_percentage
    
    elif badge.rule_type == 'perfect_score':
        return percentage == 100
    
    elif badge.rule_type == 'streak':
        # TODO: Implementar lógica de streak (sequência de acertos)
        # Por enquanto, retorna False
        return False
    
    return False


def get_user_badges_for_group(user, quiz_group):
    """
    Retorna todas as badges que o usuário tem de um grupo específico.
    
    Args:
        user: User
        quiz_group: QuizGroup
    
    Returns:
        QuerySet: UserBadges do usuário naquele grupo
    """
    return UserBadge.objects.filter(
        user=user,
        quiz_group=quiz_group
    ).select_related('badge', 'quiz_attempt__quiz')


def get_available_badges_for_group(quiz_group):
    """
    Retorna todas as badges disponíveis para um grupo.
    
    Args:
        quiz_group: QuizGroup
    
    Returns:
        QuerySet: Badges disponíveis
    """
    return Badge.objects.filter(
        quiz_groups__quiz_group=quiz_group,
        quiz_groups__active=True,
        active=True
    ).distinct()


def get_user_badge_progress(user, quiz_group):
    """
    Retorna progresso do usuário nas badges de um grupo.
    Útil para mostrar "3/5 badges conquistadas".
    
    Args:
        user: User
        quiz_group: QuizGroup
    
    Returns:
        dict: Dicionário com total, earned, percentage, remaining
    """
    total = get_available_badges_for_group(quiz_group).count()
    earned = get_user_badges_for_group(user, quiz_group).count()
    
    return {
        'total': total,
        'earned': earned,
        'percentage': (earned / total * 100) if total > 0 else 0,
        'remaining': total - earned
    }


def get_user_all_badges(user):
    """
    Retorna todas as badges do usuário, agrupadas por quiz_group.
    
    Args:
        user: User
    
    Returns:
        dict: Dicionário {quiz_group: [user_badges]}
    """
    user_badges = UserBadge.objects.filter(
        user=user
    ).select_related('badge', 'quiz_group', 'quiz_attempt__quiz').order_by('-earned_at')
    
    grouped = {}
    for user_badge in user_badges:
        group = user_badge.quiz_group
        if group not in grouped:
            grouped[group] = []
        grouped[group].append(user_badge)
    
    return grouped


def get_badge_statistics(badge):
    """
    Retorna estatísticas de uma badge.
    
    Args:
        badge: Badge
    
    Returns:
        dict: Estatísticas da badge
    """
    total_earned = UserBadge.objects.filter(badge=badge).count()
    
    # Grupos onde essa badge está disponível
    groups = badge.quiz_groups.filter(active=True).count()
    
    return {
        'total_earned': total_earned,
        'available_in_groups': groups,
        'title': badge.title,
        'rarity': badge.rarity,
    }

