import uuid
import random
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Theme(models.Model):
    COUNTRY_CHOICES = [
        ('en-US', '🇺🇸 United States'),
        ('en-CA', '🇨🇦 Canada'),
        ('es-MX', '🇲🇽 Mexico'),
        ('en-GB', '🇬🇧 United Kingdom'),
        ('de-DE', '🇩🇪 Germany'),
        ('fr-FR', '🇫🇷 France'),
        ('es-ES', '🇪🇸 Spain'),
        ('it-IT', '🇮🇹 Italy'),
        ('nl-NL', '🇳🇱 Netherlands'),
        ('sv-SE', '🇸🇪 Sweden'),
        ('no-NO', '🇳🇴 Norway'),
        ('pl-PL', '🇵🇱 Poland'),
        ('pt-PT', '🇵🇹 Portugal'),
        ('en-IN', '🇮🇳 India'),
        ('en-PH', '🇵🇭 Philippines'),
        ('id-ID', '🇮🇩 Indonesia'),
        ('ja-JP', '🇯🇵 Japan'),
        ('ko-KR', '🇰🇷 South Korea'),
        ('th-TH', '🇹🇭 Thailand'),
        ('vi-VN', '🇻🇳 Vietnam'),
        ('en-AU', '🇦🇺 Australia'),
        ('en-NZ', '🇳🇿 New Zealand'),
        ('pt-BR', '🇧🇷 Brazil'),
        ('es-AR', '🇦🇷 Argentina'),
        ('es-CO', '🇨🇴 Colombia'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    icon = models.URLField(max_length=500, blank=True, null=True, help_text='URL da imagem do ícone (PNG, SVG, etc - use Cloudinary)')
    
    # País do tema
    country = models.CharField(max_length=10, choices=COUNTRY_CHOICES, default='pt-BR', help_text='País do tema')
    
    # Cores personalizadas para a categoria na home
    primary_color = models.CharField(max_length=7, blank=True, null=True, help_text='Cor principal (ex: #3b82f6)')
    secondary_color = models.CharField(max_length=7, blank=True, null=True, help_text='Cor secundária para gradiente (ex: #8b5cf6)')
    icon_bg_color_1 = models.CharField(max_length=7, blank=True, null=True, help_text='Cor 1 do background do ícone (ex: #dbeafe)')
    icon_bg_color_2 = models.CharField(max_length=7, blank=True, null=True, help_text='Cor 2 do background do ícone (ex: #e0e7ff)')
    
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories', help_text='Tema pai (deixe vazio para categoria principal)')
    order = models.IntegerField(default=0, help_text='Ordem de exibição')
    active = models.BooleanField(default=True)
    card_background_image = models.URLField(max_length=500, blank=True, null=True, help_text='URL da imagem de background do CARD/CAIXA do tema (use Cloudinary)')
    card_background_color = models.CharField(max_length=250, blank=True, null=True, help_text='Cor de fundo do CARD/CAIXA (ex: #FF0000 ou linear-gradient(...))')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Theme"
        verbose_name_plural = "Themes"
        ordering = ['order', 'title']

    def __str__(self):
        if self.parent:
            return f"{self.parent.title} > {self.title}"
        return self.title

    def get_absolute_url(self):
        return reverse('quizzes:theme_detail', kwargs={'theme_slug': self.slug})
    
    def get_breadcrumb(self):
        """Retorna a lista de temas para o breadcrumb"""
        breadcrumb = [self]
        current = self.parent
        while current:
            breadcrumb.insert(0, current)
            current = current.parent
        return breadcrumb
    
    def is_root(self):
        """Verifica se é uma categoria principal"""
        return self.parent is None
    
    def get_children_count(self):
        """Retorna o número de subcategorias"""
        return self.subcategories.filter(active=True).count()
    
    def get_quizzes_count(self):
        """Retorna o número de quizzes ativos"""
        return self.quizzes.filter(active=True).count()


class Quiz(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Fácil'),
        ('medium', 'Médio'),
        ('hard', 'Difícil'),
    ]
    
    COUNTRY_CHOICES = Theme.COUNTRY_CHOICES

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    country = models.CharField(max_length=10, choices=COUNTRY_CHOICES, default='pt-BR', help_text='País do quiz')
    time_limit = models.IntegerField(help_text='Tempo limite em segundos (0 = sem limite)', default=0)
    question_sample_size = models.IntegerField(
        default=20,
        help_text='Número de questões aleatórias a serem selecionadas (0 = usar todas)'
    )
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
        """Retorna o total de questões cadastradas no quiz"""
        return self.questions.count()
    
    def get_questions_per_attempt(self):
        """Retorna o número de questões que serão apresentadas em cada tentativa"""
        total = self.get_total_questions()
        if self.question_sample_size > 0 and total > self.question_sample_size:
            return self.question_sample_size
        return total
    
    def get_estimated_time(self):
        """Estima o tempo em minutos baseado no número de questões por tentativa"""
        # Assumindo ~30 segundos por questão
        questions_count = self.get_questions_per_attempt()
        return max(1, round(questions_count * 0.5))  # 0.5 min = 30 segundos


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(verbose_name='Questão')
    image = models.URLField(max_length=500, blank=True, null=True, help_text='URL da imagem da questão (opcional - use Cloudinary)')
    explanation = models.TextField(blank=True, help_text='Explicação da resposta correta')
    order = models.IntegerField(default=0)
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
    question_order = models.JSONField(default=list, help_text='Ordem das questões [uuid, uuid, ...]')
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
        """Retorna as questões na ordem salva no attempt"""
        question_ids = [uuid.UUID(qid) for qid in self.question_order]
        questions = Question.objects.filter(id__in=question_ids)
        questions_dict = {str(q.id): q for q in questions}
        return [questions_dict[qid] for qid in self.question_order if qid in questions_dict]

    def initialize_question_order(self):
        """Randomiza e salva a ordem das questões"""
        questions = list(self.quiz.questions.all())
        
        # Aplicar amostragem se configurado
        sample_size = self.quiz.question_sample_size
        if sample_size > 0 and len(questions) > sample_size:
            # Selecionar aleatoriamente N questões
            questions = random.sample(questions, sample_size)
        else:
            # Usar todas as questões, apenas embaralhar
            random.shuffle(questions)
        
        self.question_order = [str(q.id) for q in questions]
        self.max_score = len(questions)
        self.save()


class UserAnswer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name='user_answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
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
        # Auto-calcular se está correto
        self.is_correct = self.selected_answer.is_correct
        super().save(*args, **kwargs)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255, verbose_name='Título do Produto')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    image_url = models.URLField(max_length=500, verbose_name='URL da Imagem (use Cloudinary)')
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
