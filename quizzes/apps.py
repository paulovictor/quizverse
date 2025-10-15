from django.apps import AppConfig


class QuizzesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quizzes'
    
    def ready(self):
        """Importa signals quando o app está pronto"""
        import quizzes.signals