from django.urls import path
from . import views

app_name = 'quizzes'

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # User Profile
    path('perfil/', views.user_profile, name='user_profile'),
    
    # Theme
    path('<slug:theme_slug>/', views.theme_detail, name='theme_detail'),
    
    # Quiz
    path('<slug:theme_slug>/<slug:quiz_slug>/', views.quiz_detail, name='quiz_detail'),
    path('<slug:theme_slug>/<slug:quiz_slug>/start/', views.quiz_start, name='quiz_start'),
    
    # Attempt (usando UUID)
    path('attempt/<uuid:attempt_id>/play/', views.quiz_play, name='quiz_play'),
    path('attempt/<uuid:attempt_id>/answer/', views.quiz_answer, name='quiz_answer'),
    path('attempt/<uuid:attempt_id>/finish/', views.quiz_finish, name='quiz_finish'),
    path('attempt/<uuid:attempt_id>/resultado/', views.quiz_result, name='quiz_result'),
    path('attempt/<uuid:attempt_id>/claim/', views.claim_attempt, name='claim_attempt'),
]

