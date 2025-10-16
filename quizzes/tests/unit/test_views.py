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


class SetCountryViewTest(TestCase):
    """Testes para view set_country"""

    def setUp(self):
        self.client = Client()
        self.url = reverse('quizzes:set_country')

    def test_set_country_changes_session(self):
        response = self.client.post(self.url, {'country': 'en-US'})
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['country'], 'en-US')

        # Verify session
        self.assertEqual(self.client.session['country'], 'en-US')

    def test_set_country_rejects_invalid_country(self):
        response = self.client.post(self.url, {'country': 'invalid'})
        self.assertEqual(response.status_code, 400)
