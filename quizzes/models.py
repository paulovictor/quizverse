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
        ('es-ES', '🇪🇸 Spain'),
        ('pt-PT', '🇵🇹 Portugal'),
        ('en-IN', '🇮🇳 India'),
        ('en-PH', '🇵🇭 Philippines'),
        ('en-AU', '🇦🇺 Australia'),
        ('en-NZ', '🇳🇿 New Zealand'),
        ('pt-BR', '🇧🇷 Brazil'),
        ('es-AR', '🇦🇷 Argentina'),
        ('es-CO', '🇨🇴 Colombia'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255, primary_key=True)
    icon = models.URLField(max_length=500, blank=True, null=True, help_text='URL da imagem do ícone (PNG, SVG, etc - use Cloudinary)')
    
    # País do tema
    country = models.CharField(max_length=10, choices=COUNTRY_CHOICES, default='pt-BR', help_text='País do tema')
    
    # Cores personalizadas para a categoria na home
    primary_color = models.CharField(max_length=7, blank=True, null=True, help_text='Cor principal (ex: #3b82f6)')
    secondary_color = models.CharField(max_length=7, blank=True, null=True, help_text='Cor secundária para gradiente (ex: #8b5cf6)')
    
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
            base_name = f"{self.parent.title} > {self.title}"
        else:
            base_name = self.title

        try:
            country_display = self.get_country_display()
            flag = country_display.split(' ')[0]
        except Exception:
            flag = ''

        if flag:
            return f"{flag} {base_name}"
        return base_name

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


class QuizGroup(models.Model):
    """Agrupa quizzes equivalentes (sempre obrigatório)"""
    DIFFICULTY_CHOICES = [
        ('easy', 'Fácil'),
        ('medium', 'Médio'),
        ('hard', 'Difícil'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name='Nome do Grupo')
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, verbose_name='Descrição')
    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES,
        default='medium',
        help_text='Dificuldade do grupo (aplicada a todos os quizzes do grupo)'
    )
    order = models.IntegerField(default=0, help_text='Ordem de exibição dos quizzes deste grupo')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Quiz Group"
        verbose_name_plural = "Quiz Groups"
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name
    
    def get_available_languages(self):
        """Retorna lista de idiomas disponíveis para este grupo"""
        return self.quizzes.filter(active=True).values_list('country', flat=True).distinct()


class Quiz(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Fácil'),
        ('medium', 'Médio'),
        ('hard', 'Difícil'),
    ]
    
    COUNTRY_CHOICES = Theme.COUNTRY_CHOICES

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='quizzes')
    quiz_group = models.ForeignKey(
        'QuizGroup',
        on_delete=models.PROTECT,
        related_name='quizzes',
        null=True,
        blank=True,
        help_text='Grupo de quizzes equivalentes (ex: mesmo quiz em vários idiomas)'
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    description_template = models.TextField(
        blank=True,
        help_text='Template de descrição com placeholders {sample_size} e {total}. Ex: "Identifique {sample_size} personagens de {total} disponíveis"'
    )
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    country = models.CharField(max_length=10, choices=COUNTRY_CHOICES, default='pt-BR', help_text='País do quiz')
    question_sample_size = models.IntegerField(
        default=0,
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

    def get_effective_difficulty(self):
        """Retorna a dificuldade efetiva: do grupo se existir, senão do quiz"""
        if self.quiz_group:
            return self.quiz_group.difficulty
        return self.difficulty

    def render_description(self):
        """Gera description a partir do template"""
        if not self.description_template:
            return self.description

        total = self.questions.count() if self.pk else 0
        sample = self.question_sample_size if self.question_sample_size > 0 else total

        try:
            return self.description_template.format(
                sample_size=sample,
                total=total
            )
        except (KeyError, ValueError):
            # Se houver erro no template, retorna a description original
            return self.description

    def save(self, *args, **kwargs):
        # Se tem template, gera description automaticamente
        if self.description_template:
            # Para novos quizzes sem questions ainda, salva sem renderizar
            if self.pk:
                self.description = self.render_description()
        super().save(*args, **kwargs)


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(verbose_name='Questão')
    image = models.URLField(max_length=500, blank=True, null=True, help_text='URL da imagem da questão (opcional - use Cloudinary)')
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

    def get_duration(self):
        """Retorna a duração do quiz em segundos, ou None se não completado"""
        if self.completed_at and self.started_at:
            delta = self.completed_at - self.started_at
            return delta.total_seconds()
        return None

    def get_duration_formatted(self):
        """Retorna a duração formatada (ex: '5min 32s', '1h 23min', '45s')"""
        duration = self.get_duration()
        if duration is None:
            return None
        
        hours = int(duration // 3600)
        minutes = int((duration % 3600) // 60)
        seconds = int(duration % 60)
        
        if hours > 0:
            return f"{hours}h {minutes}min"
        elif minutes > 0:
            return f"{minutes}min {seconds}s"
        else:
            return f"{seconds}s"

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
    discount_percentage = models.IntegerField(
        default=0, 
        verbose_name='Porcentagem de Desconto',
        help_text='Desconto em porcentagem (0-100). Use 0 para sem desconto.'
    )
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
        discount_text = f" (-{self.discount_percentage}%)" if self.discount_percentage > 0 else ""
        return f"{self.theme.title} - {self.title} (R$ {self.price}){discount_text}"


class Badge(models.Model):
    """Insignia/Badge que pode ser conquistada"""
    RULE_TYPE_CHOICES = [
        ('percentage', 'Porcentagem de Acertos'),
        ('percentage_time', 'Porcentagem + Tempo Limite'),
        ('perfect_score', 'Pontuação Perfeita'),
        ('streak', 'Sequência de Acertos'),
    ]
    
    RARITY_CHOICES = [
        ('common', 'Comum'),
        ('rare', 'Rara'),
        ('epic', 'Épica'),
        ('legendary', 'Lendária'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, verbose_name='Título da Badge')
    description = models.TextField(verbose_name='Descrição (fallback)', blank=True)
    description_translations = models.JSONField(
        default=dict,
        blank=True,
        help_text='Traduções da descrição: {"pt-BR": "texto", "en-US": "text", ...}'
    )
    image = models.URLField(max_length=500, help_text='URL da imagem da badge (Cloudinary)')
    
    # Regras
    rule_type = models.CharField(
        max_length=20, 
        choices=RULE_TYPE_CHOICES,
        default='percentage',
        verbose_name='Tipo de Regra'
    )
    min_percentage = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=0,
        help_text='Porcentagem mínima de acertos (0-100)',
        verbose_name='Porcentagem Mínima'
    )
    
    # Metadata
    rarity = models.CharField(
        max_length=20,
        choices=RARITY_CHOICES,
        default='common',
        verbose_name='Raridade'
    )
    points = models.IntegerField(default=10, help_text='Pontos que a badge vale')
    order = models.IntegerField(default=0, help_text='Ordem de exibição')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Badge"
        verbose_name_plural = "Badges"
        ordering = ['order', 'title']
    
    def __str__(self):
        return self.title
    
    def get_description(self, language=None):
        """
        Retorna a descrição traduzida para o idioma especificado.
        Se não houver tradução, retorna o fallback (campo description).
        
        Args:
            language: Código do idioma (ex: 'pt-BR', 'en-US')
        
        Returns:
            str: Descrição traduzida ou fallback
        """
        if not language:
            language = 'pt-BR'
        
        # Tenta pegar a tradução do JSONField
        if self.description_translations and language in self.description_translations:
            return self.description_translations[language]
        
        # Fallback para o campo description
        return self.description


class QuizGroupBadge(models.Model):
    """
    Define quais badges estão disponíveis para cada grupo.
    Tabela de associação simples.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quiz_group = models.ForeignKey(
        QuizGroup, 
        on_delete=models.CASCADE,
        related_name='available_badges'
    )
    badge = models.ForeignKey(
        Badge, 
        on_delete=models.CASCADE, 
        related_name='quiz_groups'
    )
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Quiz Group Badge"
        verbose_name_plural = "Quiz Group Badges"
        unique_together = ['quiz_group', 'badge']
        ordering = ['quiz_group', 'badge__order']
    
    def __str__(self):
        return f"{self.badge.title} - {self.quiz_group.name}"


class UserBadge(models.Model):
    """
    Badge conquistada por usuário.
    Campos diretos para badge e quiz_group (simplicidade e performance).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='earned_badges')
    
    # Campos diretos (performance + simplicidade)
    badge = models.ForeignKey(
        Badge,
        on_delete=models.CASCADE,
        related_name='user_achievements'
    )
    quiz_group = models.ForeignKey(
        QuizGroup,
        on_delete=models.CASCADE,
        related_name='user_achievements'
    )
    
    # Onde foi conquistada
    quiz_attempt = models.ForeignKey(
        QuizAttempt, 
        on_delete=models.CASCADE,
        related_name='badges_earned'
    )
    
    # Stats
    earned_at = models.DateTimeField(auto_now_add=True)
    score_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    completion_time_seconds = models.IntegerField(null=True, blank=True)
    
    class Meta:
        verbose_name = "User Badge"
        verbose_name_plural = "User Badges"
        ordering = ['-earned_at']
        # Garante: um usuário só ganha cada badge uma vez por grupo
        unique_together = ['user', 'badge', 'quiz_group']
        indexes = [
            models.Index(fields=['user', 'badge']),
            models.Index(fields=['user', 'quiz_group']),
            models.Index(fields=['badge', 'quiz_group']),
            models.Index(fields=['-earned_at']),
        ]
    
    def __str__(self):
        return f"{self.user.username} - {self.badge.title} ({self.quiz_group.name})"
    
    def save(self, *args, **kwargs):
        # Validação: badge deve estar disponível para o grupo
        if not QuizGroupBadge.objects.filter(
            quiz_group=self.quiz_group,
            badge=self.badge,
            active=True
        ).exists():
            raise ValueError(
                f"Badge '{self.badge}' não está disponível para o grupo '{self.quiz_group}'"
            )
        super().save(*args, **kwargs)
