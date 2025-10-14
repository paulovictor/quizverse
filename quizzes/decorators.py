"""
Custom decorators for the quizzes app
"""
from functools import wraps
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.shortcuts import redirect
from .models import QuizAttempt


def validate_attempt_access(redirect_on_error=True):
    """
    Decorator to validate that a user has permission to access a quiz attempt.
    
    For authenticated users: checks that the attempt belongs to them
    For anonymous users: checks that the session key matches
    
    Args:
        redirect_on_error: If True, redirects to theme page with error message.
                          If False, raises PermissionDenied (403).
    
    Usage:
        @validate_attempt_access()
        def my_view(request, attempt_id):
            # attempt is guaranteed to be accessible by this user
            ...
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, attempt_id, *args, **kwargs):
            attempt = get_object_or_404(QuizAttempt, id=attempt_id)
            
            # Check permissions
            has_permission = False
            
            if request.user.is_authenticated:
                # Authenticated user must own the attempt
                if attempt.user and attempt.user == request.user:
                    has_permission = True
                # Allow authenticated users to claim anonymous attempts
                elif not attempt.user:
                    has_permission = True
            else:
                # Anonymous user must match session key
                if attempt.session_key == request.session.session_key:
                    has_permission = True
            
            if not has_permission:
                if redirect_on_error:
                    messages.error(request, 'Você não tem permissão para acessar esta tentativa.')
                    return redirect('quizzes:theme_detail', theme_slug=attempt.quiz.theme.slug)
                else:
                    raise PermissionDenied('Você não tem permissão para acessar esta tentativa.')
            
            # Pass attempt to the view to avoid re-querying
            return view_func(request, attempt_id, attempt=attempt, *args, **kwargs)
        
        return wrapper
    return decorator

