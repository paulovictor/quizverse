from django.contrib import admin
from django import forms
from django.shortcuts import render, redirect
from django.urls import path
from django.contrib import messages
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import (
    Theme, Quiz, Question, Answer, QuizAttempt, UserAnswer, Product,
    Badge, QuizGroup, QuizGroupBadge, UserBadge
)


class BadgeTranslationsForm(forms.ModelForm):
    """Formulário customizado para editar traduções de badges"""
    
    class Meta:
        model = Badge
        fields = '__all__'
        widgets = {
            'description_translations': forms.Textarea(attrs={
                'rows': 10,
                'cols': 80,
                'style': 'font-family: monospace; font-size: 12px;',
                'placeholder': '{"pt-BR": "Acerte todos os 150 Pokémon! Maestria absoluta da Geração 1.", "en-US": "Get all 150 Pokémon correct! Absolute mastery of Generation 1.", "es-MX": "¡Acierta todos los 150 Pokémon! Maestría absoluta de la Generación 1."}'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.description_translations:
            # Formatar JSON para exibição mais legível
            import json
            formatted_json = json.dumps(self.instance.description_translations, indent=2, ensure_ascii=False)
            self.initial['description_translations'] = formatted_json
    
    def clean_description_translations(self):
        """Valida se o JSON das traduções é válido"""
        import json
        data = self.cleaned_data.get('description_translations')
        
        if not data:
            return {}
        
        try:
            # Se for string, tentar fazer parse
            if isinstance(data, str):
                parsed_data = json.loads(data)
            else:
                parsed_data = data
            
            # Validar se é um dicionário
            if not isinstance(parsed_data, dict):
                raise forms.ValidationError("As traduções devem ser um objeto JSON válido (dicionário).")
            
            # Validar se todos os valores são strings
            for lang, text in parsed_data.items():
                if not isinstance(text, str):
                    raise forms.ValidationError(f"O texto para '{lang}' deve ser uma string.")
                if not text.strip():
                    raise forms.ValidationError(f"O texto para '{lang}' não pode estar vazio.")
            
            return parsed_data
            
        except json.JSONDecodeError as e:
            raise forms.ValidationError(f"JSON inválido: {str(e)}")
        except Exception as e:
            raise forms.ValidationError(f"Erro ao processar traduções: {str(e)}")


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'country', 'icon', 'active', 'created_at']
    list_filter = ['active', 'country', 'created_at']
    search_fields = ['title', 'description', 'slug']  # Necessário para autocomplete
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ['parent']
    actions = ['activate_themes', 'deactivate_themes']
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'slug', 'description', 'country', 'icon', 'parent', 'order', 'active')
        }),
        ('Cores da Categoria (Home)', {
            'fields': ('primary_color', 'secondary_color'),
            'classes': ('collapse',),
            'description': 'Define as cores personalizadas da categoria na tela inicial. Use formato hexadecimal (#3b82f6).'
        }),
        ('Personalização Visual do Card', {
            'fields': ('card_background_image', 'card_background_color'),
            'classes': ('collapse',),
            'description': 'Personaliza a aparência do card/tema com imagens e cores de fundo.'
        }),
    )

    def activate_themes(self, request, queryset):
        """Ativa os temas selecionados"""
        updated = queryset.update(active=True)
        self.message_user(
            request,
            f'{updated} tema(s) foram ativados com sucesso.',
            messages.SUCCESS
        )
    activate_themes.short_description = "✅ Ativar temas selecionados"

    def deactivate_themes(self, request, queryset):
        """Inativa os temas selecionados"""
        updated = queryset.update(active=False)
        self.message_user(
            request,
            f'{updated} tema(s) foram inativados com sucesso.',
            messages.SUCCESS
        )
    deactivate_themes.short_description = "❌ Inativar temas selecionados"


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4
    fields = ['text', 'is_correct', 'order']


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    fields = ['text', 'order']
    show_change_link = True


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'theme', 'quiz_group', 'country', 'difficulty', 'active', 'get_total_questions', 'question_sample_size', 'order', 'created_at']
    list_filter = ['active', 'country', 'difficulty', 'created_at']
    search_fields = ['title', 'description', 'slug']
    autocomplete_fields = ['theme', 'quiz_group']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [QuestionInline]
    actions = ['activate_quizzes', 'deactivate_quizzes']
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'slug', 'description', 'theme', 'quiz_group', 'country', 'difficulty', 'order', 'active')
        }),
        ('Configurações do Quiz', {
            'fields': ('question_sample_size',),
            'description': 'Configure o tempo limite e quantas questões aleatórias serão apresentadas a cada tentativa. Use 0 em "question_sample_size" para usar todas as questões disponíveis.'
        }),
    )

    def activate_quizzes(self, request, queryset):
        """Ativa os quizzes selecionados"""
        updated = queryset.update(active=True)
        self.message_user(
            request,
            f'{updated} quiz(zes) foram ativados com sucesso.',
            messages.SUCCESS
        )
    activate_quizzes.short_description = "✅ Ativar quizzes selecionados"

    def deactivate_quizzes(self, request, queryset):
        """Inativa os quizzes selecionados"""
        updated = queryset.update(active=False)
        self.message_user(
            request,
            f'{updated} quiz(zes) foram inativados com sucesso.',
            messages.SUCCESS
        )
    deactivate_quizzes.short_description = "❌ Inativar quizzes selecionados"
    
    def get_total_questions(self, obj):
        return obj.get_total_questions()
    get_total_questions.short_description = 'Questões'


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['short_text', 'quiz', 'order', 'created_at']
    list_filter = ['created_at']
    search_fields = ['text', 'quiz__title']
    autocomplete_fields = ['quiz']
    inlines = [AnswerInline]
    
    def short_text(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    short_text.short_description = 'Questão'


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['short_text', 'question', 'is_correct', 'order']
    list_filter = ['is_correct', 'created_at']
    search_fields = ['text', 'question__text']
    autocomplete_fields = ['question']
    
    def short_text(self, obj):
        correct = "✓" if obj.is_correct else "✗"
        text = obj.text[:40] + '...' if len(obj.text) > 40 else obj.text
        return f"{correct} {text}"
    short_text.short_description = 'Alternativa'


class UserAnswerInline(admin.TabularInline):
    model = UserAnswer
    extra = 0
    readonly_fields = ['question', 'selected_answer', 'is_correct', 'answered_at']
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
    list_display = ['attempt_display', 'question_display', 'is_correct', 'answered_at']
    list_filter = ['is_correct', 'attempt__quiz', 'answered_at']
    search_fields = ['attempt__user__username', 'question__text']
    readonly_fields = ['attempt', 'question', 'selected_answer', 'is_correct', 'answered_at']
    
    def attempt_display(self, obj):
        return str(obj.attempt)[:50]
    attempt_display.short_description = 'Tentativa'
    
    def question_display(self, obj):
        return obj.question.text[:40] + '...' if len(obj.question.text) > 40 else obj.question.text
    question_display.short_description = 'Questão'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'theme', 'price', 'discount_percentage', 'active', 'order', 'created_at']
    list_filter = ['active', 'theme', 'created_at']
    search_fields = ['title', 'theme__title']
    list_editable = ['active', 'order', 'discount_percentage']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('theme', 'title', 'order', 'active')
        }),
        ('Preço e Desconto', {
            'fields': ('price', 'discount_percentage'),
            'description': 'Configure o preço e a porcentagem de desconto (0-100). A badge só aparece se houver desconto.'
        }),
        ('Links', {
            'fields': ('image_url', 'product_url')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class CloneQuizGroupForm(forms.Form):
    """Formulário para clonar QuizGroup com novo question_sample_size"""
    new_group_name = forms.CharField(
        label='Nome do Novo Grupo',
        max_length=255,
        help_text='Nome do novo QuizGroup que será criado'
    )
    new_group_slug = forms.SlugField(
        label='Slug do Novo Grupo',
        max_length=255,
        help_text='Slug único para o novo grupo (será usado nas URLs)'
    )
    question_sample_size = forms.IntegerField(
        label='Question Sample Size',
        min_value=0,
        help_text='Número de questões aleatórias que serão apresentadas em cada tentativa dos quizzes clonados (0 = usar todas as questões)'
    )
    clone_badges = forms.BooleanField(
        label='Clonar associações de Badges',
        required=False,
        initial=False,
        help_text='Manter as mesmas badges disponíveis para o novo grupo'
    )


@admin.register(QuizGroup)
class QuizGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'difficulty', 'order', 'get_quizzes_count', 'get_badges_count', 'created_at']
    list_editable = ['order', 'difficulty']
    list_filter = ['difficulty']
    search_fields = ['name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at']
    actions = ['clone_quizgroup_action', 'activate_all_quizzes', 'deactivate_all_quizzes']

    def get_quizzes_count(self, obj):
        return obj.quizzes.count()
    get_quizzes_count.short_description = 'Quizzes'

    def get_badges_count(self, obj):
        return obj.available_badges.filter(active=True).count()
    get_badges_count.short_description = 'Badges'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<uuid:quiz_group_id>/clone/',
                self.admin_site.admin_view(self.clone_quizgroup_view),
                name='quizzes_quizgroup_clone',
            ),
        ]
        return custom_urls + urls

    def clone_quizgroup_action(self, request, queryset):
        """Ação para clonar QuizGroup"""
        if queryset.count() != 1:
            self.message_user(
                request,
                'Selecione apenas 1 QuizGroup para clonar.',
                level=messages.ERROR
            )
            return

        quiz_group = queryset.first()
        return redirect('admin:quizzes_quizgroup_clone', quiz_group_id=quiz_group.id)

    clone_quizgroup_action.short_description = 'Clonar QuizGroup com novo sample size'

    def clone_quizgroup_view(self, request, quiz_group_id):
        """View para mostrar formulário e processar clonagem"""
        quiz_group = QuizGroup.objects.get(id=quiz_group_id)

        if request.method == 'POST':
            form = CloneQuizGroupForm(request.POST)
            if form.is_valid():
                try:
                    new_group = self._clone_quiz_group(
                        quiz_group,
                        form.cleaned_data['new_group_name'],
                        form.cleaned_data['new_group_slug'],
                        form.cleaned_data['question_sample_size'],
                        form.cleaned_data['clone_badges']
                    )

                    self.message_user(
                        request,
                        f'QuizGroup "{new_group.name}" clonado com sucesso! {new_group.quizzes.count()} quizzes criados.',
                        level=messages.SUCCESS
                    )
                    return redirect('admin:quizzes_quizgroup_change', new_group.id)

                except Exception as e:
                    self.message_user(
                        request,
                        f'Erro ao clonar QuizGroup: {str(e)}',
                        level=messages.ERROR
                    )
        else:
            # Sugerir valores padrão
            initial_data = {
                'new_group_name': f"{quiz_group.name} (Clone)",
                'new_group_slug': f"{quiz_group.slug}-clone",
                'question_sample_size': 20,
                'clone_badges': False,
            }
            form = CloneQuizGroupForm(initial=initial_data)

        context = {
            'form': form,
            'quiz_group': quiz_group,
            'quizzes_count': quiz_group.quizzes.count(),
            'title': f'Clonar QuizGroup: {quiz_group.name}',
            'site_title': self.admin_site.site_title,
            'site_header': self.admin_site.site_header,
            'opts': self.model._meta,
        }

        return render(request, 'admin/quizzes/clone_quizgroup.html', context)

    def _clone_quiz_group(self, original_group, new_name, new_slug, question_sample_size, clone_badges):
        """Clona o QuizGroup e todos os seus quizzes"""

        # 1. Criar novo QuizGroup
        new_group = QuizGroup.objects.create(
            name=new_name,
            slug=new_slug,
            description=original_group.description
        )

        # 2. Clonar todos os quizzes do grupo original
        original_quizzes = original_group.quizzes.all()

        for original_quiz in original_quizzes:
            # Gerar novo slug para o quiz clonado
            new_quiz_slug = f"{original_quiz.slug}-{new_slug.split('-')[-1]}"

            # Criar novo quiz (INATIVO por padrão)
            new_quiz = Quiz.objects.create(
                theme=original_quiz.theme,
                quiz_group=new_group,
                title=original_quiz.title,
                slug=new_quiz_slug,
                description=original_quiz.description,
                description_template=original_quiz.description_template,  # Copia o template
                difficulty=original_quiz.difficulty,
                country=original_quiz.country,
                question_sample_size=question_sample_size,  # NOVO VALOR
                active=False,  # Criar como inativo
                order=original_quiz.order,
            )

            # 3. Clonar todas as questões e respostas
            original_questions = original_quiz.questions.all()

            for original_question in original_questions:
                new_question = Question.objects.create(
                    quiz=new_quiz,
                    text=original_question.text,
                    image=original_question.image,
                    order=original_question.order,
                )

                # Clonar respostas
                original_answers = original_question.answers.all()
                for original_answer in original_answers:
                    Answer.objects.create(
                        question=new_question,
                        text=original_answer.text,
                        is_correct=original_answer.is_correct,
                        order=original_answer.order,
                    )

            # 4. Atualizar description se tem template (agora que as questões foram criadas)
            if new_quiz.description_template:
                new_quiz.save()  # Vai renderizar o template com o novo sample_size

        # 4. Clonar associações de badges (se solicitado)
        if clone_badges:
            original_badge_associations = original_group.available_badges.all()
            for badge_assoc in original_badge_associations:
                QuizGroupBadge.objects.create(
                    quiz_group=new_group,
                    badge=badge_assoc.badge,
                    active=badge_assoc.active,
                )

        return new_group

    def activate_all_quizzes(self, request, queryset):
        """Ativa todos os quizzes dos QuizGroups selecionados"""
        total_updated = 0
        groups_processed = 0

        for quiz_group in queryset:
            updated = quiz_group.quizzes.update(active=True)
            total_updated += updated
            groups_processed += 1

        self.message_user(
            request,
            f'{total_updated} quizzes ativados em {groups_processed} grupo(s).',
            level=messages.SUCCESS
        )

    activate_all_quizzes.short_description = 'Ativar todos os quizzes dos grupos selecionados'

    def deactivate_all_quizzes(self, request, queryset):
        """Desativa todos os quizzes dos QuizGroups selecionados"""
        total_updated = 0
        groups_processed = 0

        for quiz_group in queryset:
            updated = quiz_group.quizzes.update(active=False)
            total_updated += updated
            groups_processed += 1

        self.message_user(
            request,
            f'{total_updated} quizzes desativados em {groups_processed} grupo(s).',
            level=messages.WARNING
        )

    deactivate_all_quizzes.short_description = 'Desativar todos os quizzes dos grupos selecionados'


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    form = BadgeTranslationsForm
    list_display = ['title', 'rule_type', 'min_percentage', 'rarity', 'points', 'active', 'order', 'translations_count']
    list_filter = ['active', 'rule_type', 'rarity', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['active', 'order']
    readonly_fields = ['created_at', 'translations_preview']
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'description', 'image', 'order', 'active')
        }),
        ('Traduções', {
            'fields': ('description_translations', 'translations_preview'),
            'description': 'Adicione traduções da descrição para diferentes idiomas. Use o formato JSON válido: {"pt-BR": "texto", "en-US": "text", ...}'
        }),
        ('Regras da Badge', {
            'fields': ('rule_type', 'min_percentage'),
            'description': 'Defina os critérios para conquistar esta badge. Para "percentage_time", preencha ambos os campos.'
        }),
        ('Metadata', {
            'fields': ('rarity', 'points'),
            'classes': ('collapse',),
        }),
    )
    
    def translations_count(self, obj):
        """Mostra quantas traduções existem"""
        if obj.description_translations:
            return f"{len(obj.description_translations)} idiomas"
        return "0 idiomas"
    translations_count.short_description = 'Traduções'
    
    def translations_preview(self, obj):
        """Mostra preview das traduções"""
        if not obj.description_translations:
            return "Nenhuma tradução disponível"
        
        preview_items = []
        for lang, text in obj.description_translations.items():
            # Truncar texto longo
            short_text = text[:50] + "..." if len(text) > 50 else text
            preview_items.append(format_html("<strong>{}:</strong> {}", lang, short_text))
        
        return format_html("<br>".join(preview_items))
    translations_preview.short_description = 'Preview das Traduções'


class QuizGroupBadgeInline(admin.TabularInline):
    model = QuizGroupBadge
    extra = 1
    fields = ['badge', 'active']


@admin.register(QuizGroupBadge)
class QuizGroupBadgeAdmin(admin.ModelAdmin):
    list_display = ['badge', 'quiz_group', 'active', 'created_at']
    list_filter = ['active', 'quiz_group', 'badge', 'created_at']
    search_fields = ['badge__title', 'quiz_group__name']
    list_editable = ['active']
    readonly_fields = ['created_at']


@admin.register(UserBadge)
class UserBadgeAdmin(admin.ModelAdmin):
    list_display = ['user', 'badge', 'quiz_group', 'score_percentage', 'completion_time_display', 'earned_at']
    list_filter = ['badge', 'quiz_group', 'earned_at']
    search_fields = ['user__username', 'badge__title', 'quiz_group__name']
    readonly_fields = ['user', 'badge', 'quiz_group', 'quiz_attempt', 'earned_at', 'score_percentage', 'completion_time_seconds']
    
    def completion_time_display(self, obj):
        if obj.completion_time_seconds:
            minutes = int(obj.completion_time_seconds // 60)
            seconds = int(obj.completion_time_seconds % 60)
            if minutes > 0:
                return f"{minutes}min {seconds}s"
            return f"{seconds}s"
        return "-"
    completion_time_display.short_description = 'Tempo'
    
    def has_add_permission(self, request):
        # Não permitir adicionar badges manualmente (devem ser conquistadas)
        return False
    
    def has_delete_permission(self, request, obj=None):
        # Permitir apenas para superusuários
        return request.user.is_superuser
