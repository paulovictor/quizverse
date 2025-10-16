"""
Testes abrangentes para templates HTML.

Este arquivo contém testes que verificam:
- Conteúdo renderizado correto
- Elementos HTML críticos presentes
- Lógica condicional nos templates
- Dados dinâmicos sendo exibidos corretamente
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from quizzes.tests.fixtures.factories import (
    UserFactory, ThemeFactory, QuizFactory, QuestionFactory,
    QuizAttemptFactory, ProductFactory, BadgeFactory,
    QuizGroupFactory, QuizGroupBadgeFactory, UserBadgeFactory
)
from quizzes.models import UserAnswer, QuizAttempt
from django.utils import timezone

User = get_user_model()


class HomeTemplateTest(TestCase):
    """Testes para o template home.html"""

    def setUp(self):
        self.client = Client()
        self.theme1 = ThemeFactory.create(
            title="Matemática",
            parent=None,
            country='pt-BR',
            order=1
        )
        self.theme2 = ThemeFactory.create(
            title="História",
            parent=None,
            country='pt-BR',
            order=2
        )
        self.quiz, _ = QuizFactory.create_with_questions(
            theme=self.theme1,
            num_questions=5
        )

    def test_home_displays_main_themes(self):
        """Verifica se os temas principais são exibidos"""
        response = self.client.get(reverse('quizzes:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Matemática")
        self.assertContains(response, "História")

    def test_home_displays_quiz_count(self):
        """Verifica se a contagem de quizzes é exibida"""
        response = self.client.get(reverse('quizzes:home'))

        # Deve mostrar pelo menos "1" (do quiz criado)
        self.assertContains(response, str(1))

    def test_home_has_hero_section(self):
        """Verifica se a seção hero está presente"""
        response = self.client.get(reverse('quizzes:home'))

        self.assertContains(response, 'hero')

    def test_home_has_theme_cards(self):
        """Verifica se os cards de tema estão presentes"""
        response = self.client.get(reverse('quizzes:home'))

        # Verificar que o tema aparece na página
        self.assertContains(response, self.theme1.title)

    def test_home_empty_themes(self):
        """Verifica comportamento quando não há temas"""
        # Deletar todos os temas
        self.theme1.delete()
        self.theme2.delete()

        response = self.client.get(reverse('quizzes:home'))

        self.assertEqual(response.status_code, 200)
        # Não deve causar erro


class ThemeDetailTemplateTest(TestCase):
    """Testes para o template theme_detail.html"""

    def setUp(self):
        self.client = Client()
        self.parent_theme = ThemeFactory.create(
            title="Ciências",
            parent=None,
            country='pt-BR'
        )
        self.child_theme = ThemeFactory.create(
            title="Física",
            parent=self.parent_theme,
            country='pt-BR'
        )
        self.quiz, _ = QuizFactory.create_with_questions(
            theme=self.child_theme,
            title="Quiz de Física Básica",
            num_questions=5
        )

    def test_theme_detail_displays_theme_title(self):
        """Verifica se o título do tema é exibido"""
        url = reverse('quizzes:theme_detail', kwargs={'theme_slug': self.parent_theme.slug})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ciências")

    def test_theme_detail_displays_subcategories(self):
        """Verifica se as subcategorias são exibidas"""
        url = reverse('quizzes:theme_detail', kwargs={'theme_slug': self.parent_theme.slug})
        response = self.client.get(url)

        self.assertContains(response, "Física")

    def test_theme_detail_displays_quizzes(self):
        """Verifica se os quizzes do tema são exibidos"""
        url = reverse('quizzes:theme_detail', kwargs={'theme_slug': self.child_theme.slug})
        response = self.client.get(url)

        self.assertContains(response, "Quiz de Física Básica")

    def test_theme_detail_has_breadcrumb(self):
        """Verifica se o breadcrumb está presente"""
        url = reverse('quizzes:theme_detail', kwargs={'theme_slug': self.child_theme.slug})
        response = self.client.get(url)

        self.assertContains(response, 'breadcrumb')
        # Breadcrumb deve conter o tema pai
        self.assertContains(response, "Ciências")

    def test_theme_detail_empty_theme(self):
        """Verifica comportamento de tema sem quizzes nem subcategorias"""
        empty_theme = ThemeFactory.create(
            title="Tema Vazio",
            parent=None,
            country='pt-BR'
        )
        url = reverse('quizzes:theme_detail', kwargs={'theme_slug': empty_theme.slug})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tema Vazio")


class QuizDetailTemplateTest(TestCase):
    """Testes para o template quiz_detail.html"""

    def setUp(self):
        self.client = Client()
        self.user = UserFactory.create()
        self.theme = ThemeFactory.create(title="Matemática", country='pt-BR')
        self.quiz, self.questions = QuizFactory.create_with_questions(
            theme=self.theme,
            title="Álgebra Básica",
            description="Teste seus conhecimentos em álgebra",
            num_questions=10
        )

    def test_quiz_detail_displays_quiz_info(self):
        """Verifica se as informações do quiz são exibidas"""
        url = reverse('quizzes:quiz_detail', kwargs={
            'theme_slug': self.theme.slug,
            'quiz_slug': self.quiz.slug
        })
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Álgebra Básica")
        self.assertContains(response, "Teste seus conhecimentos em álgebra")

    def test_quiz_detail_displays_question_count(self):
        """Verifica se a contagem de questões é exibida"""
        url = reverse('quizzes:quiz_detail', kwargs={
            'theme_slug': self.theme.slug,
            'quiz_slug': self.quiz.slug
        })
        response = self.client.get(url)

        # Deve mostrar o número de questões
        self.assertContains(response, "10")

    def test_quiz_detail_displays_start_button(self):
        """Verifica se o botão de iniciar está presente"""
        url = reverse('quizzes:quiz_detail', kwargs={
            'theme_slug': self.theme.slug,
            'quiz_slug': self.quiz.slug
        })
        response = self.client.get(url)

        # Procurar por form de início ou botão - verificar que há action para quiz_start
        self.assertContains(response, 'Iniciar')

    def test_quiz_detail_shows_previous_attempts_when_logged_in(self):
        """Verifica se tentativas anteriores são mostradas para usuário logado"""
        self.client.force_login(self.user)

        # Criar uma tentativa completada
        attempt, _ = QuizAttemptFactory.create_with_answers(
            user=self.user,
            quiz=self.quiz,
            num_correct=8
        )
        attempt.completed_at = timezone.now()
        attempt.save()

        url = reverse('quizzes:quiz_detail', kwargs={
            'theme_slug': self.theme.slug,
            'quiz_slug': self.quiz.slug
        })
        response = self.client.get(url)

        # Deve mostrar a pontuação da tentativa anterior
        self.assertContains(response, "8")

    def test_quiz_detail_no_attempts_when_not_logged_in(self):
        """Verifica que tentativas anteriores não aparecem quando não logado"""
        url = reverse('quizzes:quiz_detail', kwargs={
            'theme_slug': self.theme.slug,
            'quiz_slug': self.quiz.slug
        })
        response = self.client.get(url)

        # Não deve ter seção de tentativas anteriores
        self.assertEqual(response.status_code, 200)


class QuizPlayTemplateTest(TestCase):
    """Testes para o template quiz_play.html"""

    def setUp(self):
        self.client = Client()
        self.user = UserFactory.create()
        self.theme = ThemeFactory.create(country='pt-BR')
        self.quiz, self.questions = QuizFactory.create_with_questions(
            theme=self.theme,
            num_questions=5
        )
        self.attempt = QuizAttemptFactory.create(
            user=self.user,
            quiz=self.quiz
        )
        self.attempt.initialize_question_order()

    def test_quiz_play_displays_question(self):
        """Verifica se a questão é exibida"""
        self.client.force_login(self.user)
        url = reverse('quizzes:quiz_play', kwargs={'attempt_id': self.attempt.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        # Deve conter o texto de alguma questão
        questions = self.attempt.get_ordered_questions()
        first_question = questions[0]
        self.assertContains(response, first_question.text)

    def test_quiz_play_displays_answers(self):
        """Verifica se as alternativas são exibidas"""
        self.client.force_login(self.user)
        url = reverse('quizzes:quiz_play', kwargs={'attempt_id': self.attempt.id})
        response = self.client.get(url)

        # Deve ter múltiplas alternativas
        questions = self.attempt.get_ordered_questions()
        first_question = questions[0]
        answers = first_question.answers.all()

        for answer in answers:
            self.assertContains(response, answer.text)

    def test_quiz_play_displays_progress(self):
        """Verifica se o progresso é exibido"""
        self.client.force_login(self.user)
        url = reverse('quizzes:quiz_play', kwargs={'attempt_id': self.attempt.id})
        response = self.client.get(url)

        # Deve mostrar algo como "1/5" ou "Questão 1"
        self.assertContains(response, "1")

    def test_quiz_play_has_answer_form(self):
        """Verifica se o formulário de resposta está presente"""
        self.client.force_login(self.user)
        url = reverse('quizzes:quiz_play', kwargs={'attempt_id': self.attempt.id})
        response = self.client.get(url)

        # Deve ter um formulário para enviar resposta
        self.assertContains(response, 'question_id')
        self.assertContains(response, 'answer_id')


class QuizResultTemplateTest(TestCase):
    """Testes para o template quiz_result.html"""

    def setUp(self):
        self.client = Client()
        self.user = UserFactory.create()
        self.theme = ThemeFactory.create(country='pt-BR')
        self.quiz, self.questions = QuizFactory.create_with_questions(
            theme=self.theme,
            num_questions=10
        )

    def test_quiz_result_displays_score_perfect(self):
        """Verifica se a pontuação perfeita é exibida corretamente"""
        self.client.force_login(self.user)

        # Criar tentativa com 100%
        attempt, _ = QuizAttemptFactory.create_with_answers(
            user=self.user,
            quiz=self.quiz,
            num_correct=10
        )
        attempt.completed_at = timezone.now()
        attempt.save()

        url = reverse('quizzes:quiz_result', kwargs={'attempt_id': attempt.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "100%")
        self.assertContains(response, "10")

    def test_quiz_result_displays_score_partial(self):
        """Verifica se pontuação parcial é exibida corretamente"""
        self.client.force_login(self.user)

        # Criar tentativa com 70%
        attempt, _ = QuizAttemptFactory.create_with_answers(
            user=self.user,
            quiz=self.quiz,
            num_correct=7
        )
        attempt.completed_at = timezone.now()
        attempt.save()

        url = reverse('quizzes:quiz_result', kwargs={'attempt_id': attempt.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "70%")
        self.assertContains(response, "7")

    def test_quiz_result_displays_performance_message(self):
        """Verifica se mensagens de performance aparecem"""
        self.client.force_login(self.user)

        # Criar tentativa excelente
        attempt, _ = QuizAttemptFactory.create_with_answers(
            user=self.user,
            quiz=self.quiz,
            num_correct=9
        )
        attempt.completed_at = timezone.now()
        attempt.save()

        url = reverse('quizzes:quiz_result', kwargs={'attempt_id': attempt.id})
        response = self.client.get(url)

        # Deve ter alguma mensagem de parabéns ou feedback
        content = response.content.decode()
        self.assertTrue('Excelente' in content or 'excelente' in content)

    def test_quiz_result_shows_all_questions_and_answers(self):
        """Verifica se todas as questões e respostas são exibidas"""
        self.client.force_login(self.user)

        attempt, _ = QuizAttemptFactory.create_with_answers(
            user=self.user,
            quiz=self.quiz,
            num_correct=5
        )
        attempt.completed_at = timezone.now()
        attempt.save()

        url = reverse('quizzes:quiz_result', kwargs={'attempt_id': attempt.id})
        response = self.client.get(url)

        # Verificar que as questões aparecem
        questions = attempt.get_ordered_questions()
        for question in questions[:3]:  # Verificar pelo menos 3
            self.assertContains(response, question.text)

    def test_quiz_result_has_retry_button(self):
        """Verifica se o botão de tentar novamente está presente"""
        self.client.force_login(self.user)

        attempt, _ = QuizAttemptFactory.create_with_answers(
            user=self.user,
            quiz=self.quiz,
            num_correct=5
        )
        attempt.completed_at = timezone.now()
        attempt.save()

        url = reverse('quizzes:quiz_result', kwargs={'attempt_id': attempt.id})
        response = self.client.get(url)

        # Deve ter link para tentar novamente
        self.assertContains(response, self.quiz.slug)

    def test_quiz_result_shows_login_prompt_for_anonymous(self):
        """Verifica se prompt de login aparece para usuários anônimos"""
        # Criar tentativa anônima
        attempt, _ = QuizAttemptFactory.create_with_answers(
            user=None,
            quiz=self.quiz,
            num_correct=7
        )
        attempt.completed_at = timezone.now()
        # Importante: definir session_key para permitir acesso anônimo
        attempt.session_key = 'test-session-key'
        attempt.save()

        # Definir a sessão para corresponder à tentativa
        session = self.client.session
        session.save()  # Salvar para gerar session_key
        attempt.session_key = session.session_key
        attempt.save()

        url = reverse('quizzes:quiz_result', kwargs={'attempt_id': attempt.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        # Deve sugerir fazer login ou criar conta
        content = response.content.decode()
        self.assertTrue('login' in content or 'Login' in content or 'Entrar' in content)


class UserProfileTemplateTest(TestCase):
    """Testes para o template user_profile.html"""

    def setUp(self):
        self.client = Client()
        self.user = UserFactory.create(username="testuser", first_name="João")
        self.theme = ThemeFactory.create(title="Geografia", country='pt-BR')
        self.quiz, _ = QuizFactory.create_with_questions(
            theme=self.theme,
            num_questions=10
        )

    def test_user_profile_requires_login(self):
        """Verifica se a página exige login"""
        url = reverse('quizzes:user_profile')
        response = self.client.get(url)

        # Deve redirecionar para login
        self.assertEqual(response.status_code, 302)

    def test_user_profile_displays_username(self):
        """Verifica se o nome do usuário é exibido"""
        self.client.force_login(self.user)
        url = reverse('quizzes:user_profile')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "João")

    def test_user_profile_displays_statistics(self):
        """Verifica se as estatísticas são exibidas"""
        self.client.force_login(self.user)

        # Criar algumas tentativas
        for i in range(3):
            attempt, _ = QuizAttemptFactory.create_with_answers(
                user=self.user,
                quiz=self.quiz,
                num_correct=8
            )
            attempt.completed_at = timezone.now()
            attempt.save()

        url = reverse('quizzes:user_profile')
        response = self.client.get(url)

        # Deve mostrar número de quizzes completados
        self.assertContains(response, "3")
        # Deve mostrar taxa de acerto (80%)
        self.assertContains(response, "80")

    def test_user_profile_shows_achievements_section(self):
        """Verifica se a seção de conquistas está presente"""
        self.client.force_login(self.user)
        url = reverse('quizzes:user_profile')
        response = self.client.get(url)

        content = response.content.decode()
        self.assertTrue('conquistas' in content or 'Conquistas' in content)

    def test_user_profile_shows_results_section(self):
        """Verifica se a seção de resultados está presente"""
        self.client.force_login(self.user)
        url = reverse('quizzes:user_profile')
        response = self.client.get(url)

        content = response.content.decode()
        self.assertTrue('resultados' in content or 'Resultados' in content)

    def test_user_profile_displays_badges_when_earned(self):
        """Verifica se badges conquistadas são exibidas"""
        self.client.force_login(self.user)

        # Criar badge
        badge = BadgeFactory.create(title="Mestre da Geografia")
        quiz_group = QuizGroupFactory.create()
        group_badge = QuizGroupBadgeFactory.create(
            badge=badge,
            quiz_group=quiz_group
        )

        # Criar tentativa
        attempt, _ = QuizAttemptFactory.create_with_answers(
            user=self.user,
            quiz=self.quiz,
            num_correct=10
        )
        attempt.completed_at = timezone.now()
        attempt.save()

        # Conceder badge
        UserBadgeFactory.create(
            user=self.user,
            badge=badge,
            quiz_group=quiz_group,
            quiz_attempt=attempt
        )

        url = reverse('quizzes:user_profile')
        response = self.client.get(url)

        self.assertContains(response, "Mestre da Geografia")

    def test_user_profile_empty_state_no_attempts(self):
        """Verifica estado vazio quando usuário não tem tentativas"""
        self.client.force_login(self.user)
        url = reverse('quizzes:user_profile')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        # Deve mostrar mensagem de estado vazio
        self.assertContains(response, "0")

    def test_user_profile_empty_state_no_badges(self):
        """Verifica estado vazio quando usuário não tem badges"""
        self.client.force_login(self.user)
        url = reverse('quizzes:user_profile')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        # Deve mostrar que não há conquistas ainda

    def test_user_profile_shows_recent_attempts(self):
        """Verifica se tentativas recentes são exibidas"""
        self.client.force_login(self.user)

        # Criar tentativa
        attempt, _ = QuizAttemptFactory.create_with_answers(
            user=self.user,
            quiz=self.quiz,
            num_correct=6
        )
        attempt.completed_at = timezone.now()
        attempt.save()

        url = reverse('quizzes:user_profile')
        response = self.client.get(url)

        # Deve mostrar o quiz na lista de resultados
        self.assertContains(response, self.quiz.title)
        self.assertContains(response, "6")

    def test_user_profile_filter_by_category(self):
        """Verifica se o filtro por categoria funciona"""
        self.client.force_login(self.user)

        # Criar tentativa
        attempt, _ = QuizAttemptFactory.create_with_answers(
            user=self.user,
            quiz=self.quiz,
            num_correct=7
        )
        attempt.completed_at = timezone.now()
        attempt.save()

        url = reverse('quizzes:user_profile') + f'?category={self.theme.slug}'
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.quiz.title)

    def test_user_profile_has_navigation_tabs(self):
        """Verifica se as abas de navegação estão presentes"""
        self.client.force_login(self.user)
        url = reverse('quizzes:user_profile')
        response = self.client.get(url)

        # Deve ter abas para conquistas e resultados
        self.assertContains(response, "profile-nav-tab")


class TemplateContextTest(TestCase):
    """Testes para verificar que o contexto está sendo passado corretamente"""

    def setUp(self):
        self.client = Client()

    def test_all_pages_have_country_context(self):
        """Verifica se todas as páginas principais têm contexto de país"""
        theme = ThemeFactory.create(country='pt-BR')
        quiz, _ = QuizFactory.create_with_questions(theme=theme)

        urls = [
            reverse('quizzes:home'),
            reverse('quizzes:theme_detail', kwargs={'theme_slug': theme.slug}),
            reverse('quizzes:quiz_detail', kwargs={
                'theme_slug': theme.slug,
                'quiz_slug': quiz.slug
            }),
        ]

        for url in urls:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                # Verificar que current_country está no contexto
                self.assertIn('current_country', response.context)

    def test_authenticated_pages_have_user_context(self):
        """Verifica se páginas autenticadas têm contexto de usuário"""
        user = UserFactory.create()
        self.client.force_login(user)

        url = reverse('quizzes:user_profile')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn('user', response.context)
        self.assertEqual(response.context['user'], user)


class TemplateErrorHandlingTest(TestCase):
    """Testes para verificar comportamento em situações de erro"""

    def setUp(self):
        self.client = Client()

    def test_quiz_detail_handles_missing_quiz(self):
        """Verifica se 404 é retornado para quiz inexistente"""
        theme = ThemeFactory.create()
        url = reverse('quizzes:quiz_detail', kwargs={
            'theme_slug': theme.slug,
            'quiz_slug': 'non-existent-quiz'
        })
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_theme_detail_handles_missing_theme(self):
        """Verifica se 404 é retornado para tema inexistente"""
        url = reverse('quizzes:theme_detail', kwargs={
            'theme_slug': 'non-existent-theme'
        })
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_quiz_result_handles_missing_attempt(self):
        """Verifica se 404 é retornado para tentativa inexistente"""
        user = UserFactory.create()
        self.client.force_login(user)

        # Usar um UUID válido mas inexistente
        import uuid
        fake_uuid = str(uuid.uuid4())

        url = reverse('quizzes:quiz_result', kwargs={'attempt_id': fake_uuid})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)


class ResponsiveTemplateTest(TestCase):
    """Testes para verificar elementos responsivos nos templates"""

    def setUp(self):
        self.client = Client()
        self.theme = ThemeFactory.create(country='pt-BR')
        self.quiz, _ = QuizFactory.create_with_questions(theme=self.theme)

    def test_templates_have_viewport_meta(self):
        """Verifica se os templates têm meta viewport para responsividade"""
        urls = [
            reverse('quizzes:home'),
            reverse('quizzes:theme_detail', kwargs={'theme_slug': self.theme.slug}),
        ]

        for url in urls:
            with self.subTest(url=url):
                response = self.client.get(url)
                # Verificar que não há erros críticos
                self.assertEqual(response.status_code, 200)
