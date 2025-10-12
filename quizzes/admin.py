from django.contrib import admin
from .models import Theme, Quiz, Question, Answer, QuizAttempt, UserAnswer, Product


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'active', 'created_at']
    list_filter = ['active', 'created_at']
    search_fields = ['title', 'description', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4
    fields = ['text', 'is_correct', 'order']


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    fields = ['text', 'explanation', 'order', 'points']
    show_change_link = True


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'theme', 'difficulty', 'active', 'get_total_questions', 'order', 'created_at']
    list_filter = ['active', 'difficulty', 'theme', 'created_at']
    search_fields = ['title', 'description', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [QuestionInline]
    
    def get_total_questions(self, obj):
        return obj.get_total_questions()
    get_total_questions.short_description = 'Perguntas'


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['short_text', 'quiz', 'order', 'points', 'created_at']
    list_filter = ['quiz__theme', 'quiz', 'created_at']
    search_fields = ['text', 'explanation']
    inlines = [AnswerInline]
    
    def short_text(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    short_text.short_description = 'Pergunta'


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['short_text', 'question', 'is_correct', 'order']
    list_filter = ['is_correct', 'question__quiz']
    search_fields = ['text']
    
    def short_text(self, obj):
        correct = "✓" if obj.is_correct else "✗"
        text = obj.text[:40] + '...' if len(obj.text) > 40 else obj.text
        return f"{correct} {text}"
    short_text.short_description = 'Alternativa'


class UserAnswerInline(admin.TabularInline):
    model = UserAnswer
    extra = 0
    readonly_fields = ['question', 'selected_answer', 'is_correct', 'points_earned', 'answered_at']
    can_delete = False


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'quiz', 'score', 'max_score', 'percentage', 'is_completed', 'started_at']
    list_filter = ['quiz__theme', 'quiz', 'completed_at', 'started_at']
    search_fields = ['user__username', 'session_key', 'ip_address']
    readonly_fields = ['started_at', 'question_order', 'ip_address', 'session_key']
    inlines = [UserAnswerInline]
    
    def user_display(self, obj):
        if obj.user:
            return obj.user.username
        return f"Anônimo ({obj.session_key[:8]}...)"
    user_display.short_description = 'Usuário'
    
    def percentage(self, obj):
        return f"{obj.get_score_percentage()}%"
    percentage.short_description = '%'
    
    def is_completed(self, obj):
        return obj.is_completed()
    is_completed.boolean = True
    is_completed.short_description = 'Completo'


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ['attempt_display', 'question_display', 'is_correct', 'points_earned', 'answered_at']
    list_filter = ['is_correct', 'attempt__quiz', 'answered_at']
    search_fields = ['attempt__user__username', 'question__text']
    readonly_fields = ['attempt', 'question', 'selected_answer', 'is_correct', 'points_earned', 'answered_at']
    
    def attempt_display(self, obj):
        return str(obj.attempt)[:50]
    attempt_display.short_description = 'Tentativa'
    
    def question_display(self, obj):
        return obj.question.text[:40] + '...' if len(obj.question.text) > 40 else obj.question.text
    question_display.short_description = 'Pergunta'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'theme', 'price', 'active', 'order', 'created_at']
    list_filter = ['active', 'theme', 'created_at']
    search_fields = ['title', 'theme__title']
    list_editable = ['active', 'order']
    readonly_fields = ['created_at', 'updated_at']
