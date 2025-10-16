"""
Testes de integração para fluxo completo de quiz
"""
from django.test import TestCase, Client
from django.urls import reverse
from quizzes.models import QuizAttempt, UserAnswer
from quizzes.tests.fixtures.factories import (
    UserFactory, ThemeFactory, QuizFactory, QuestionFactory, QuizGroupFactory, BadgeFactory, QuizGroupBadgeFactory
)


class CompleteQuizFlowTest(TestCase):
    """Testa fluxo completo: iniciar -> responder -> finalizar -> resultado"""

    def setUp(self):
        self.client = Client()
        self.user = UserFactory.create()
        self.theme = ThemeFactory.create()
        self.quiz, self.questions = QuizFactory.create_with_questions(
            theme=self.theme,
            num_questions=5
        )

    def test_complete_quiz_flow_authenticated(self):
        """Testa fluxo completo para usuário autenticado"""
        self.client.force_login(self.user)

        # 1. Ver página do quiz
        detail_url = reverse('quizzes:quiz_detail', kwargs={
            'theme_slug': self.theme.slug,
            'quiz_slug': self.quiz.slug
        })
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, 200)

        # 2. Iniciar quiz
        start_url = reverse('quizzes:quiz_start', kwargs={
            'theme_slug': self.theme.slug,
            'quiz_slug': self.quiz.slug
        })
        response = self.client.post(start_url)
        self.assertEqual(response.status_code, 302)

        # Obter attempt criado
        attempt = QuizAttempt.objects.filter(user=self.user, quiz=self.quiz).first()
        self.assertIsNotNone(attempt)

        # 3. Responder todas as questões
        for question in self.questions:
            correct_answer = question.get_correct_answer()
            answer_url = reverse('quizzes:quiz_answer', kwargs={'attempt_id': attempt.id})

            response = self.client.post(answer_url, {
                'question_id': str(question.id),
                'answer_id': str(correct_answer.id)
            })
            self.assertEqual(response.status_code, 200)

        # Verificar que todas foram respondidas
        self.assertEqual(UserAnswer.objects.filter(attempt=attempt).count(), 5)

        # 4. Finalizar
        finish_url = reverse('quizzes:quiz_finish', kwargs={'attempt_id': attempt.id})
        response = self.client.get(finish_url)
        self.assertEqual(response.status_code, 302)

        # 5. Ver resultado
        result_url = reverse('quizzes:quiz_result', kwargs={'attempt_id': attempt.id})
        response = self.client.get(result_url)
        self.assertEqual(response.status_code, 200)

        # Verificar que tentativa foi completada
        attempt.refresh_from_db()
        self.assertTrue(attempt.is_completed())
        self.assertEqual(attempt.score, 5)  # Todas corretas

    def test_complete_quiz_flow_anonymous(self):
        """Testa fluxo completo para usuário anônimo"""
        # Não fazer login

        # Iniciar quiz
        start_url = reverse('quizzes:quiz_start', kwargs={
            'theme_slug': self.theme.slug,
            'quiz_slug': self.quiz.slug
        })
        response = self.client.post(start_url)
        self.assertEqual(response.status_code, 302)

        # Verificar que attempt foi criado sem user
        attempt = QuizAttempt.objects.filter(quiz=self.quiz, user__isnull=True).first()
        self.assertIsNotNone(attempt)
        self.assertIsNone(attempt.user)
        self.assertIsNotNone(attempt.session_key)


class BadgeAwardingFlowTest(TestCase):
    """Testa fluxo de concessão de badges"""

    def setUp(self):
        self.client = Client()
        self.user = UserFactory.create()
        self.quiz_group = QuizGroupFactory.create()
        self.theme = ThemeFactory.create()
        self.quiz, self.questions = QuizFactory.create_with_questions(
            theme=self.theme,
            quiz_group=self.quiz_group,
            num_questions=10
        )

        # Criar badge
        self.badge = BadgeFactory.create(
            title="80% Master",
            rule_type='percentage',
            min_percentage=80
        )
        QuizGroupBadgeFactory.create(quiz_group=self.quiz_group, badge=self.badge)

    def test_badge_awarded_on_completion(self):
        """Testa que badge é concedida ao completar com 80%+"""
        self.client.force_login(self.user)

        # Iniciar quiz
        start_url = reverse('quizzes:quiz_start', kwargs={
            'theme_slug': self.theme.slug,
            'quiz_slug': self.quiz.slug
        })
        response = self.client.post(start_url)
        attempt = QuizAttempt.objects.get(user=self.user, quiz=self.quiz)

        # Responder 8/10 corretas (80%)
        for i, question in enumerate(self.questions):
            if i < 8:  # 8 corretas
                answer = question.get_correct_answer()
            else:  # 2 erradas
                answer = question.answers.filter(is_correct=False).first()

            self.client.post(
                reverse('quizzes:quiz_answer', kwargs={'attempt_id': attempt.id}),
                {'question_id': str(question.id), 'answer_id': str(answer.id)}
            )

        # Finalizar
        self.client.get(reverse('quizzes:quiz_finish', kwargs={'attempt_id': attempt.id}))

        # Acessar página de resultado (é aqui que badges são concedidas)
        self.client.get(reverse('quizzes:quiz_result', kwargs={'attempt_id': attempt.id}))

        # Verificar badge concedida
        from quizzes.models import UserBadge
        user_badges = UserBadge.objects.filter(user=self.user, badge=self.badge)
        self.assertEqual(user_badges.count(), 1)

    def test_badge_not_awarded_below_threshold(self):
        """Testa que badge NÃO é concedida abaixo de 80%"""
        self.client.force_login(self.user)

        start_url = reverse('quizzes:quiz_start', kwargs={
            'theme_slug': self.theme.slug,
            'quiz_slug': self.quiz.slug
        })
        response = self.client.post(start_url)
        attempt = QuizAttempt.objects.get(user=self.user, quiz=self.quiz)

        # Responder apenas 7/10 (70%)
        for i, question in enumerate(self.questions):
            if i < 7:
                answer = question.get_correct_answer()
            else:
                answer = question.answers.filter(is_correct=False).first()

            self.client.post(
                reverse('quizzes:quiz_answer', kwargs={'attempt_id': attempt.id}),
                {'question_id': str(question.id), 'answer_id': str(answer.id)}
            )

        self.client.get(reverse('quizzes:quiz_finish', kwargs={'attempt_id': attempt.id}))

        # Acessar página de resultado
        self.client.get(reverse('quizzes:quiz_result', kwargs={'attempt_id': attempt.id}))

        # Verificar que badge NÃO foi concedida
        from quizzes.models import UserBadge
        user_badges = UserBadge.objects.filter(user=self.user, badge=self.badge)
        self.assertEqual(user_badges.count(), 0)


class MultipleAttemptsTest(TestCase):
    """Testa múltiplas tentativas do mesmo quiz"""

    def setUp(self):
        self.client = Client()
        self.user = UserFactory.create()
        self.theme = ThemeFactory.create()
        self.quiz, self.questions = QuizFactory.create_with_questions(theme=self.theme)

    def test_multiple_attempts_allowed(self):
        """Testa que usuário pode fazer múltiplas tentativas"""
        self.client.force_login(self.user)

        start_url = reverse('quizzes:quiz_start', kwargs={
            'theme_slug': self.theme.slug,
            'quiz_slug': self.quiz.slug
        })

        # Primeira tentativa
        self.client.post(start_url)
        # Segunda tentativa
        self.client.post(start_url)

        attempts = QuizAttempt.objects.filter(user=self.user, quiz=self.quiz)
        self.assertEqual(attempts.count(), 2)
