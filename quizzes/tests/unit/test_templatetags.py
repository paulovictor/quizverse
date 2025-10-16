"""
Testes unitários para template tags e filtros
"""
from django.test import TestCase
from django.template import Context, Template
from quizzes.templatetags import icon_tags, translations
from quizzes.tests.fixtures.factories import ThemeFactory, BadgeFactory


class RenderIconTagTest(TestCase):
    """Testes para tag render_icon"""

    def test_render_icon_with_image(self):
        theme = ThemeFactory.create(icon="https://example.com/icon.png")
        result = icon_tags.render_icon(theme)

        self.assertIn('<img', result)
        self.assertIn('https://example.com/icon.png', result)
        self.assertIn(theme.title, result)

    def test_render_icon_without_image(self):
        theme = ThemeFactory.create(icon=None)
        result = icon_tags.render_icon(theme)

        self.assertIn('📚', result)
        self.assertIn('theme-icon-placeholder', result)

    def test_render_icon_with_custom_class(self):
        theme = ThemeFactory.create(icon="https://example.com/icon.png")
        result = icon_tags.render_icon(theme, css_class='custom-class')

        self.assertIn('custom-class', result)


class HasIconFilterTest(TestCase):
    """Testes para filtro has_icon"""

    def test_has_icon_true(self):
        theme = ThemeFactory.create(icon="https://example.com/icon.png")
        self.assertTrue(icon_tags.has_icon(theme))

    def test_has_icon_false(self):
        theme = ThemeFactory.create(icon=None)
        self.assertFalse(icon_tags.has_icon(theme))


class BadgeDescriptionFilterTest(TestCase):
    """Testes para filtro badge_description"""

    def test_badge_description_default_language(self):
        badge = BadgeFactory.create(
            description_translations={
                'pt-BR': 'Descrição em português',
                'en-US': 'Description in English'
            }
        )

        result = icon_tags.badge_description(badge, 'pt-BR')
        self.assertEqual(result, 'Descrição em português')

    def test_badge_description_fallback(self):
        badge = BadgeFactory.create(description="Default description")
        result = icon_tags.badge_description(badge, 'fr-FR')
        self.assertEqual(result, 'Default description')


class TranslationTagTest(TestCase):
    """Testes para template tag de tradução"""

    def test_translation_tag_in_template(self):
        template = Template("{% load icon_tags %}{% t 'home' %}")
        context = Context({'current_language': 'pt'})
        rendered = template.render(context)

        self.assertIsNotNone(rendered)
        self.assertGreater(len(rendered.strip()), 0)

    def test_translation_filter(self):
        result = icon_tags.translate('home', 'pt')
        self.assertIsNotNone(result)
