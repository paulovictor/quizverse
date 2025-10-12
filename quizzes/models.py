import uuid
import random
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Theme(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True, max_length=255)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Theme"
        verbose_name_plural = "Themes"
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('quizzes:theme_detail', kwargs={'theme_slug': self.slug})


class Quiz(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Fácil'),
        ('medium', 'Médio'),
        ('hard', 'Difícil'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    time_limit = models.IntegerField(help_text='Tempo limite em segundos (0 = sem limite)', default=0)
    active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"
        unique_together = ['theme', 'slug']
        ordering = ['theme', 'order', 'title']

    def __str__(self):
        return f"{self.theme.title} - {self.title}"

    def get_absolute_url(self):
        return reverse('quizzes:quiz_detail', kwargs={
            'theme_slug': self.theme.slug,
            'quiz_slug': self.slug
        })

    def get_total_questions(self):
        return self.questions.count()

    def get_total_points(self):
        return self.questions.aggregate(total=models.Sum('points'))['total'] or 0


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(verbose_name='Pergunta')
    explanation = models.TextField(blank=True, help_text='Explicação da resposta correta')
    order = models.IntegerField(default=0)
    points = models.IntegerField(default=1, help_text='Pontos por acertar essa questão')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ['quiz', 'order']

    def __str__(self):
        return f"{self.quiz.title} - Q{self.order}: {self.text[:50]}"

    def get_correct_answer(self):
        return self.answers.filter(is_correct=True).first()


class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=500, verbose_name='Alternativa')
    is_correct = models.BooleanField(default=False, verbose_name='É a resposta correta?')
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
        ordering = ['question', 'order']

    def __str__(self):
        correct = "✓" if self.is_correct else "✗"
        return f"{correct} {self.text[:50]}"


class QuizAttempt(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='quiz_attempts')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='attempts')
    session_key = models.CharField(max_length=40, blank=True, help_text='Para usuários não logados')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    question_order = models.JSONField(default=list, help_text='Ordem das perguntas [uuid, uuid, ...]')
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField(default=0)
    max_score = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Quiz Attempt"
        verbose_name_plural = "Quiz Attempts"
        ordering = ['-started_at']

    def __str__(self):
        user_str = self.user.username if self.user else f"Anonymous ({self.session_key[:8]})"
        return f"{user_str} - {self.quiz.title} - {self.started_at.strftime('%Y-%m-%d %H:%M')}"

    def is_completed(self):
        return self.completed_at is not None

    def get_score_percentage(self):
        if self.max_score == 0:
            return 0
        return round((self.score / self.max_score) * 100, 1)

    def get_ordered_questions(self):
        """Retorna as perguntas na ordem salva no attempt"""
        question_ids = [uuid.UUID(qid) for qid in self.question_order]
        questions = Question.objects.filter(id__in=question_ids)
        questions_dict = {str(q.id): q for q in questions}
        return [questions_dict[qid] for qid in self.question_order if qid in questions_dict]

    def initialize_question_order(self):
        """Randomiza e salva a ordem das perguntas"""
        questions = list(self.quiz.questions.all())
        random.shuffle(questions)
        self.question_order = [str(q.id) for q in questions]
        self.max_score = sum(q.points for q in questions)
        self.save()


class UserAnswer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name='user_answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    points_earned = models.IntegerField(default=0)
    answered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "User Answer"
        verbose_name_plural = "User Answers"
        unique_together = ['attempt', 'question']
        ordering = ['answered_at']

    def __str__(self):
        correct = "✓" if self.is_correct else "✗"
        return f"{correct} {self.attempt} - {self.question.text[:30]}"

    def save(self, *args, **kwargs):
        # Auto-calcular se está correto e os pontos
        self.is_correct = self.selected_answer.is_correct
        self.points_earned = self.question.points if self.is_correct else 0
        super().save(*args, **kwargs)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255, verbose_name='Título do Produto')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    image_url = models.URLField(max_length=500, verbose_name='URL da Imagem')
    product_url = models.URLField(max_length=500, verbose_name='Link do Produto')
    active = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text='Ordem de exibição')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['theme', 'order', 'title']

    def __str__(self):
        return f"{self.theme.title} - {self.title} (R$ {self.price})"
