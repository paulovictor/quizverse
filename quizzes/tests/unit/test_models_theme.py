"""
Testes unitários para o model Theme
"""
from django.test import TestCase
from django.urls import reverse
from quizzes.models import Theme
from quizzes.tests.fixtures.factories import ThemeFactory, QuizFactory


class ThemeModelTest(TestCase):
    """Testes para o model Theme"""

    def setUp(self):
        """Setup para cada teste"""
        self.theme = ThemeFactory.create(
            title="Test Theme",
            description="Test Description",
            country='pt-BR'
        )

    def test_theme_creation(self):
        """Testa criação básica de um tema"""
        self.assertIsNotNone(self.theme.slug)
        self.assertEqual(self.theme.title, "Test Theme")
        self.assertEqual(self.theme.country, 'pt-BR')
        self.assertTrue(self.theme.active)

    def test_theme_str_representation(self):
        """Testa representação em string"""
        str_repr = str(self.theme)
        self.assertIn("Test Theme", str_repr)
        self.assertIn("🇧🇷", str_repr)  # Flag do Brasil

    def test_theme_str_with_parent(self):
        """Testa string representation com tema pai"""
        child = ThemeFactory.create(
            title="Child Theme",
            parent=self.theme
        )
        str_repr = str(child)
        self.assertIn("Test Theme", str_repr)
        self.assertIn("Child Theme", str_repr)
        self.assertIn(">", str_repr)

    def test_theme_absolute_url(self):
        """Testa get_absolute_url"""
        url = self.theme.get_absolute_url()
        expected_url = reverse('quizzes:theme_detail', kwargs={'theme_slug': self.theme.slug})
        self.assertEqual(url, expected_url)

    def test_theme_is_root_true(self):
        """Testa is_root() para tema sem parent"""
        self.assertTrue(self.theme.is_root())

    def test_theme_is_root_false(self):
        """Testa is_root() para tema com parent"""
        child = ThemeFactory.create(parent=self.theme)
        self.assertFalse(child.is_root())

    def test_theme_get_breadcrumb_single(self):
        """Testa breadcrumb para tema único"""
        breadcrumb = self.theme.get_breadcrumb()
        self.assertEqual(len(breadcrumb), 1)
        self.assertEqual(breadcrumb[0], self.theme)

    def test_theme_get_breadcrumb_nested(self):
        """Testa breadcrumb para temas aninhados"""
        child = ThemeFactory.create(title="Child", parent=self.theme)
        grandchild = ThemeFactory.create(title="Grandchild", parent=child)

        breadcrumb = grandchild.get_breadcrumb()
        self.assertEqual(len(breadcrumb), 3)
        self.assertEqual(breadcrumb[0], self.theme)
        self.assertEqual(breadcrumb[1], child)
        self.assertEqual(breadcrumb[2], grandchild)

    def test_theme_get_children_count(self):
        """Testa contagem de subcategorias"""
        self.assertEqual(self.theme.get_children_count(), 0)

        # Adicionar filhos
        ThemeFactory.create(parent=self.theme)
        ThemeFactory.create(parent=self.theme)

        self.assertEqual(self.theme.get_children_count(), 2)

    def test_theme_get_children_count_only_active(self):
        """Testa que get_children_count conta apenas ativos"""
        ThemeFactory.create(parent=self.theme, active=True)
        ThemeFactory.create(parent=self.theme, active=False)

        self.assertEqual(self.theme.get_children_count(), 1)

    def test_theme_get_quizzes_count(self):
        """Testa contagem de quizzes"""
        self.assertEqual(self.theme.get_quizzes_count(), 0)

        # Adicionar quizzes
        QuizFactory.create(theme=self.theme)
        QuizFactory.create(theme=self.theme)

        self.assertEqual(self.theme.get_quizzes_count(), 2)

    def test_theme_get_quizzes_count_only_active(self):
        """Testa que get_quizzes_count conta apenas ativos"""
        QuizFactory.create(theme=self.theme, active=True)
        QuizFactory.create(theme=self.theme, active=False)

        self.assertEqual(self.theme.get_quizzes_count(), 1)

    def test_theme_ordering(self):
        """Testa ordenação de temas"""
        theme1 = ThemeFactory.create(title="B Theme", order=2)
        theme2 = ThemeFactory.create(title="A Theme", order=1)
        theme3 = ThemeFactory.create(title="C Theme", order=1)

        # Filtrar apenas os themes criados neste teste
        themes = list(Theme.objects.filter(
            id__in=[theme1.id, theme2.id, theme3.id]
        ).order_by('order', 'title'))

        # Verificar ordenação
        self.assertEqual(len(themes), 3)
        self.assertEqual(themes[0], theme2)  # order=1, title="A Theme"
        self.assertEqual(themes[1], theme3)  # order=1, title="C Theme"
        self.assertEqual(themes[2], theme1)  # order=2, title="B Theme"

    def test_theme_custom_colors(self):
        """Testa cores personalizadas"""
        theme = ThemeFactory.create(
            primary_color="#3b82f6",
            secondary_color="#8b5cf6",
        )

        self.assertEqual(theme.primary_color, "#3b82f6")
        self.assertEqual(theme.secondary_color, "#8b5cf6")

    def test_theme_with_icon(self):
        """Testa tema com ícone"""
        theme = ThemeFactory.create(
            icon="https://example.com/icon.png"
        )
        self.assertEqual(theme.icon, "https://example.com/icon.png")

    def test_theme_with_card_background(self):
        """Testa tema com background de card"""
        theme = ThemeFactory.create(
            card_background_image="https://example.com/bg.jpg",
            card_background_color="linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
        )
        self.assertEqual(theme.card_background_image, "https://example.com/bg.jpg")
        self.assertIn("linear-gradient", theme.card_background_color)

    def test_theme_country_choices(self):
        """Testa que os países suportados existem"""
        self.assertIsNotNone(Theme.COUNTRY_CHOICES)
        self.assertGreater(len(Theme.COUNTRY_CHOICES), 0)

        # Verificar alguns países
        countries = [choice[0] for choice in Theme.COUNTRY_CHOICES]
        self.assertIn('pt-BR', countries)
        self.assertIn('en-US', countries)
        self.assertIn('es-MX', countries)

    def test_theme_different_countries(self):
        """Testa criação de temas para diferentes países"""
        theme_br = ThemeFactory.create(title="Tema BR", country='pt-BR')
        theme_us = ThemeFactory.create(title="Theme US", country='en-US')
        theme_mx = ThemeFactory.create(title="Tema MX", country='es-MX')

        self.assertEqual(theme_br.country, 'pt-BR')
        self.assertEqual(theme_us.country, 'en-US')
        self.assertEqual(theme_mx.country, 'es-MX')

    def test_theme_unique_slug(self):
        """Testa que slug é único"""
        theme1 = ThemeFactory.create(slug="unique-slug")

        from django.db import IntegrityError
        with self.assertRaises(IntegrityError):
            ThemeFactory.create(slug="unique-slug")

    def test_theme_auto_timestamps(self):
        """Testa created_at e updated_at automáticos"""
        self.assertIsNotNone(self.theme.created_at)
        self.assertIsNotNone(self.theme.updated_at)
        # Timestamps podem ter microsegundos diferentes
        self.assertAlmostEqual(
            self.theme.created_at.timestamp(),
            self.theme.updated_at.timestamp(),
            places=0
        )

    def test_theme_cascade_delete_with_quizzes(self):
        """Testa deleção em cascata com quizzes"""
        quiz = QuizFactory.create(theme=self.theme)
        quiz_id = quiz.id

        self.theme.delete()

        from quizzes.models import Quiz
        self.assertFalse(Quiz.objects.filter(id=quiz_id).exists())
