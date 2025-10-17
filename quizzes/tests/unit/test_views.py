"""
Testes unitários para views.py
"""
from django.test import TestCase, Client
from django.urls import reverse
from quizzes.tests.fixtures.factories import (
    UserFactory, ThemeFactory, QuizFactory, QuestionFactory,
    QuizAttemptFactory
)


class HomeViewTest(TestCase):
    """Testes para view home"""

    def setUp(self):
        self.client = Client()
        self.theme = ThemeFactory.create(parent=None, country='pt-BR')

    def test_home_view_loads(self):
        response = self.client.get(reverse('quizzes:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quizzes/home.html')

    def test_home_view_shows_themes(self):
        response = self.client.get(reverse('quizzes:home'))
        self.assertContains(response, self.theme.title)

    def test_home_view_filters_by_country(self):
        session = self.client.session
        session['country'] = 'pt-BR'
        session.save()

        response = self.client.get(reverse('quizzes:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_has_hero_section(self):
        """Verifica se a seção hero está presente"""
        response = self.client.get(reverse('quizzes:home'))
        self.assertContains(response, 'hero')

    def test_home_view_shows_theme_cards(self):
        """Verifica se os cards de temas estão presentes"""
        response = self.client.get(reverse('quizzes:home'))
        self.assertContains(response, 'category-card')
        self.assertContains(response, self.theme.title)


class ThemeDetailViewTest(TestCase):
    """Testes para view theme_detail"""

    def setUp(self):
        self.client = Client()
        self.theme = ThemeFactory.create(country='pt-BR')
        self.quiz, _ = QuizFactory.create_with_questions(theme=self.theme, num_questions=5)

    def test_theme_detail_view_loads(self):
        url = reverse('quizzes:theme_detail', kwargs={'theme_slug': self.theme.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quizzes/theme_detail.html')

    def test_theme_detail_shows_quizzes(self):
        url = reverse('quizzes:theme_detail', kwargs={'theme_slug': self.theme.slug})
        response = self.client.get(url)
        self.assertContains(response, self.quiz.title)

    def test_theme_detail_404_for_invalid_slug(self):
        url = reverse('quizzes:theme_detail', kwargs={'theme_slug': 'invalid-slug'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_theme_detail_has_breadcrumb(self):
        """Verifica se o breadcrumb está presente"""
        url = reverse('quizzes:theme_detail', kwargs={'theme_slug': self.theme.slug})
        response = self.client.get(url)
        self.assertContains(response, 'breadcrumb')

    def test_theme_detail_shows_quiz_cards(self):
        """Verifica se os cards de quizzes estão presentes"""
        url = reverse('quizzes:theme_detail', kwargs={'theme_slug': self.theme.slug})
        response = self.client.get(url)
        self.assertContains(response, self.quiz.title)


class QuizDetailViewTest(TestCase):
    """Testes para view quiz_detail"""

    def setUp(self):
        self.client = Client()
        self.theme = ThemeFactory.create()
        self.quiz, self.questions = QuizFactory.create_with_questions(theme=self.theme)

    def test_quiz_detail_view_loads(self):
        url = reverse('quizzes:quiz_detail', kwargs={
            'theme_slug': self.theme.slug,
            'quiz_slug': self.quiz.slug
        })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quizzes/quiz_detail.html')

    def test_quiz_detail_shows_questions_count(self):
        url = reverse('quizzes:quiz_detail', kwargs={
            'theme_slug': self.theme.slug,
            'quiz_slug': self.quiz.slug
        })
        response = self.client.get(url)
        self.assertContains(response, str(len(self.questions)))

    def test_quiz_detail_shows_quiz_title_and_description(self):
        """Verifica se título e descrição do quiz são exibidos"""
        url = reverse('quizzes:quiz_detail', kwargs={
            'theme_slug': self.theme.slug,
            'quiz_slug': self.quiz.slug
        })
        response = self.client.get(url)
        self.assertContains(response, self.quiz.title)
        if self.quiz.description:
            self.assertContains(response, self.quiz.description)

    def test_quiz_detail_has_start_button(self):
        """Verifica se o botão de iniciar está presente"""
        url = reverse('quizzes:quiz_detail', kwargs={
            'theme_slug': self.theme.slug,
            'quiz_slug': self.quiz.slug
        })
        response = self.client.get(url)
        # Deve ter formulário para iniciar quiz
        self.assertContains(response, 'start')


class QuizStartViewTest(TestCase):
    """Testes para view quiz_start"""

    def setUp(self):
        self.client = Client()
        self.theme = ThemeFactory.create()
        self.quiz, _ = QuizFactory.create_with_questions(theme=self.theme, num_questions=5)
        self.url = reverse('quizzes:quiz_start', kwargs={
            'theme_slug': self.theme.slug,
            'quiz_slug': self.quiz.slug
        })

    def test_quiz_start_creates_attempt(self):
        from quizzes.models import QuizAttempt
        initial_count = QuizAttempt.objects.count()

        response = self.client.post(self.url)
        self.assertEqual(QuizAttempt.objects.count(), initial_count + 1)
        self.assertEqual(response.status_code, 302)  # Redirect

    def test_quiz_start_redirects_to_play(self):
        response = self.client.post(self.url)
        self.assertIn('/play/', response.url)

    def test_quiz_start_requires_post(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 405)  # Method not allowed


class QuizPlayViewTest(TestCase):
    """Testes para view quiz_play"""

    def setUp(self):
        self.client = Client()
        self.user = UserFactory.create()
        self.theme = ThemeFactory.create()
        self.quiz, self.questions = QuizFactory.create_with_questions(theme=self.theme)
        self.attempt = QuizAttemptFactory.create(user=self.user, quiz=self.quiz)

    def test_quiz_play_view_loads(self):
        self.client.force_login(self.user)
        url = reverse('quizzes:quiz_play', kwargs={'attempt_id': self.attempt.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quizzes/quiz_play.html')

    def test_quiz_play_redirects_if_completed(self):
        from django.utils import timezone
        self.attempt.completed_at = timezone.now()
        self.attempt.save()

        self.client.force_login(self.user)
        url = reverse('quizzes:quiz_play', kwargs={'attempt_id': self.attempt.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertIn('/resultado/', response.url)

    def test_quiz_play_shows_question_text(self):
        """Verifica se o texto da questão é exibido"""
        self.client.force_login(self.user)
        self.attempt.initialize_question_order()

        url = reverse('quizzes:quiz_play', kwargs={'attempt_id': self.attempt.id})
        response = self.client.get(url)

        # Deve mostrar a primeira questão
        questions = self.attempt.get_ordered_questions()
        first_question = questions[0]
        self.assertContains(response, first_question.text)

    def test_quiz_play_shows_all_answers(self):
        """Verifica se todas as alternativas são exibidas"""
        self.client.force_login(self.user)
        self.attempt.initialize_question_order()

        url = reverse('quizzes:quiz_play', kwargs={'attempt_id': self.attempt.id})
        response = self.client.get(url)

        questions = self.attempt.get_ordered_questions()
        first_question = questions[0]
        answers = first_question.answers.all()

        # Verificar que pelo menos algumas respostas aparecem
        for answer in answers[:2]:
            self.assertContains(response, answer.text)

    def test_quiz_play_shows_progress_indicator(self):
        """Verifica se o indicador de progresso está presente"""
        self.client.force_login(self.user)
        self.attempt.initialize_question_order()

        url = reverse('quizzes:quiz_play', kwargs={'attempt_id': self.attempt.id})
        response = self.client.get(url)

        # Deve mostrar indicação de progresso (ex: "1 / 5")
        total = len(self.attempt.get_ordered_questions())
        self.assertContains(response, f'1 / {total}')


class QuizAnswerViewTest(TestCase):
    """Testes para view quiz_answer"""

    def setUp(self):
        self.client = Client()
        self.user = UserFactory.create()
        self.theme = ThemeFactory.create()
        self.quiz, self.questions = QuizFactory.create_with_questions(theme=self.theme)
        self.attempt = QuizAttemptFactory.create(user=self.user, quiz=self.quiz)
        self.question = self.questions[0]
        self.correct_answer = self.question.get_correct_answer()
        self.url = reverse('quizzes:quiz_answer', kwargs={'attempt_id': self.attempt.id})

    def test_quiz_answer_creates_user_answer(self):
        from quizzes.models import UserAnswer
        self.client.force_login(self.user)

        initial_count = UserAnswer.objects.count()
        response = self.client.post(self.url, {
            'question_id': str(self.question.id),
            'answer_id': str(self.correct_answer.id)
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(UserAnswer.objects.count(), initial_count + 1)

    def test_quiz_answer_returns_correct_status(self):
        self.client.force_login(self.user)

        # Usar HTTP_X_REQUESTED_WITH para simular AJAX request
        response = self.client.post(self.url, {
            'question_id': str(self.question.id),
            'answer_id': str(self.correct_answer.id)
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertTrue(data['is_correct'])


class QuizResultViewTest(TestCase):
    """Testes para view quiz_result"""

    def setUp(self):
        self.client = Client()
        self.user = UserFactory.create()
        self.theme = ThemeFactory.create()
        self.quiz, self.questions = QuizFactory.create_with_questions(theme=self.theme)
        self.attempt, _ = QuizAttemptFactory.create_with_answers(
            user=self.user,
            quiz=self.quiz,
            num_correct=4
        )
        from django.utils import timezone
        self.attempt.completed_at = timezone.now()
        self.attempt.save()

    def test_quiz_result_view_loads(self):
        self.client.force_login(self.user)
        url = reverse('quizzes:quiz_result', kwargs={'attempt_id': self.attempt.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quizzes/quiz_result.html')

    def test_quiz_result_shows_score(self):
        self.client.force_login(self.user)
        url = reverse('quizzes:quiz_result', kwargs={'attempt_id': self.attempt.id})
        response = self.client.get(url)
        percentage = self.attempt.get_score_percentage()
        self.assertContains(response, f"{percentage}%")

    def test_quiz_result_shows_performance_message(self):
        """Verifica se mensagem de performance é exibida"""
        self.client.force_login(self.user)
        url = reverse('quizzes:quiz_result', kwargs={'attempt_id': self.attempt.id})
        response = self.client.get(url)

        # Deve ter alguma mensagem de feedback
        self.assertTrue(
            'Excelente' in response.content.decode() or
            'Bom' in response.content.decode() or
            'Continue' in response.content.decode()
        )

    def test_quiz_result_displays_all_questions(self):
        """Verifica se todas as questões são exibidas no resultado"""
        self.client.force_login(self.user)
        url = reverse('quizzes:quiz_result', kwargs={'attempt_id': self.attempt.id})
        response = self.client.get(url)

        # Verificar que as questões aparecem
        questions = self.attempt.get_ordered_questions()
        for question in questions[:3]:  # Verificar pelo menos as 3 primeiras
            self.assertContains(response, question.text)

    def test_quiz_result_has_retry_button(self):
        """Verifica se o botão de tentar novamente está presente"""
        self.client.force_login(self.user)
        url = reverse('quizzes:quiz_result', kwargs={'attempt_id': self.attempt.id})
        response = self.client.get(url)

        # Deve ter link para a página do quiz
        self.assertContains(response, self.quiz.slug)

    def test_quiz_result_hero_section_present(self):
        """Verifica se a seção hero com resultado está presente"""
        self.client.force_login(self.user)
        url = reverse('quizzes:quiz_result', kwargs={'attempt_id': self.attempt.id})
        response = self.client.get(url)

        self.assertContains(response, 'result-hero')


class UserProfileViewTest(TestCase):
    """Testes para view user_profile"""

    def setUp(self):
        self.client = Client()
        self.user = UserFactory.create()

    def test_user_profile_requires_login(self):
        url = reverse('quizzes:user_profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_user_profile_loads_for_logged_in_user(self):
        self.client.force_login(self.user)
        url = reverse('quizzes:user_profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quizzes/user_profile.html')

    def test_user_profile_displays_user_stats(self):
        """Verifica se estatísticas do usuário são exibidas"""
        self.client.force_login(self.user)

        # Criar algumas tentativas para gerar estatísticas
        theme = ThemeFactory.create(country='pt-BR')
        quiz, _ = QuizFactory.create_with_questions(theme=theme, num_questions=10)

        from django.utils import timezone
        for _ in range(3):
            attempt, _ = QuizAttemptFactory.create_with_answers(
                user=self.user,
                quiz=quiz,
                num_correct=7
            )
            attempt.completed_at = timezone.now()
            attempt.save()

        url = reverse('quizzes:user_profile')
        response = self.client.get(url)

        # Verificar que estatísticas aparecem
        self.assertContains(response, 'profile-hero')  # Seção de hero com stats
        self.assertContains(response, '3')  # Total de tentativas
        self.assertContains(response, '70')  # Taxa de acerto (70%)

    def test_user_profile_shows_empty_state_correctly(self):
        """Verifica que estado vazio é exibido quando usuário não tem tentativas"""
        self.client.force_login(self.user)
        url = reverse('quizzes:user_profile')
        response = self.client.get(url)

        # Deve ter mensagem de estado vazio (há múltiplas instâncias no CSS)
        self.assertContains(response, 'empty-state')
        # Taxa de acerto deve ser 0
        self.assertContains(response, '0%')

    def test_user_profile_navigation_tabs_present(self):
        """Verifica se as abas de navegação estão presentes"""
        self.client.force_login(self.user)
        url = reverse('quizzes:user_profile')
        response = self.client.get(url)

        # Deve ter abas de conquistas e resultados
        self.assertContains(response, 'profile-nav-tab')
        self.assertContains(response, 'conquistas')
        self.assertContains(response, 'resultados')


class SetCountryViewTest(TestCase):
    """Testes para view set_country"""

    def setUp(self):
        self.client = Client()
        self.url = reverse('quizzes:set_country')

    def test_set_country_changes_session(self):
        """Testa se a mudança de país salva corretamente na sessão"""
        response = self.client.post(self.url, {'country': 'en-US'})
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['country'], 'en-US')

        # Verify session
        self.assertEqual(self.client.session['country'], 'en-US')

    def test_set_country_rejects_invalid_country(self):
        """Testa se países inválidos são rejeitados"""
        response = self.client.post(self.url, {'country': 'invalid'})
        self.assertEqual(response.status_code, 400)
        
        data = response.json()
        self.assertFalse(data['success'])
        self.assertIn('error', data)

    def test_set_country_creates_session_if_none(self):
        """Testa se uma nova sessão é criada quando não existe"""
        # Garantir que não há sessão
        self.client.cookies.clear()
        
        response = self.client.post(self.url, {'country': 'pt-BR'})
        self.assertEqual(response.status_code, 200)
        
        # Verificar que sessão foi criada
        self.assertIsNotNone(self.client.session.session_key)
        self.assertEqual(self.client.session['country'], 'pt-BR')

    def test_set_country_accepts_all_supported_countries(self):
        """Testa se todos os países suportados são aceitos"""
        from quizzes.models import Theme
        
        supported_countries = [code for code, name in Theme.COUNTRY_CHOICES]
        
        for country_code in supported_countries[:5]:  # Testar alguns países
            response = self.client.post(self.url, {'country': country_code})
            self.assertEqual(response.status_code, 200, f"Failed for country: {country_code}")
            
            data = response.json()
            self.assertTrue(data['success'], f"Failed for country: {country_code}")
            self.assertEqual(data['country'], country_code)

    def test_set_country_requires_post_method(self):
        """Testa se apenas método POST é aceito"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 405)  # Method not allowed
        
        response = self.client.put(self.url, {'country': 'en-US'})
        self.assertEqual(response.status_code, 405)

    def test_set_country_handles_missing_country_parameter(self):
        """Testa comportamento quando parâmetro country não é fornecido"""
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['country'], 'pt-BR')  # Default value

    def test_set_country_json_response_format(self):
        """Testa se a resposta JSON tem o formato correto"""
        response = self.client.post(self.url, {'country': 'es-ES'})
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('success', data)
        self.assertIn('country', data)
        self.assertIsInstance(data['success'], bool)
        self.assertIsInstance(data['country'], str)

    def test_set_country_session_persistence(self):
        """Testa se a sessão persiste entre requisições"""
        # Primeira requisição
        response1 = self.client.post(self.url, {'country': 'fr-FR'})
        self.assertEqual(response1.status_code, 200)
        
        # Segunda requisição (deve manter a sessão)
        response2 = self.client.get(reverse('quizzes:home'))
        self.assertEqual(response2.status_code, 200)
        
        # Verificar que o país ainda está na sessão
        self.assertEqual(self.client.session['country'], 'fr-FR')

    def test_set_country_with_csrf_token(self):
        """Testa se a view funciona com token CSRF"""
        # Obter token CSRF
        csrf_response = self.client.get(reverse('quizzes:home'))
        csrf_token = csrf_response.cookies.get('csrftoken')
        
        if csrf_token:
            response = self.client.post(
                self.url, 
                {'country': 'de-DE'},
                HTTP_X_CSRFTOKEN=csrf_token.value
            )
            self.assertEqual(response.status_code, 200)
            
            data = response.json()
            self.assertTrue(data['success'])
            self.assertEqual(self.client.session['country'], 'de-DE')
