"""
Testes unitários para QuizAttempt e UserAnswer
"""
from django.test import TestCase
from django.utils import timezone
from quizzes.models import QuizAttempt, UserAnswer
from quizzes.tests.fixtures.factories import (
    QuizAttemptFactory, UserAnswerFactory, UserFactory,
    QuizFactory, QuestionFactory, AnswerFactory
)


class QuizAttemptModelTest(TestCase):
    """Testes para QuizAttempt"""

    def setUp(self):
        self.user = UserFactory.create()
        self.quiz, self.questions = QuizFactory.create_with_questions(num_questions=10)
        self.attempt = QuizAttemptFactory.create(user=self.user, quiz=self.quiz)

    def test_attempt_creation(self):
        """Testa criação básica"""
        self.assertIsNotNone(self.attempt.id)
        self.assertEqual(self.attempt.user, self.user)
        self.assertEqual(self.attempt.quiz, self.quiz)
        self.assertIsNotNone(self.attempt.started_at)

    def test_attempt_str_representation(self):
        """Testa string representation"""
        str_repr = str(self.attempt)
        self.assertIn(self.user.username, str_repr)
        self.assertIn(self.quiz.title, str_repr)

    def test_attempt_is_completed_false(self):
        """Testa is_completed quando não finalizado"""
        self.assertFalse(self.attempt.is_completed())
        self.assertIsNone(self.attempt.completed_at)

    def test_attempt_is_completed_true(self):
        """Testa is_completed quando finalizado"""
        self.attempt.completed_at = timezone.now()
        self.attempt.save()
        self.assertTrue(self.attempt.is_completed())

    def test_attempt_get_score_percentage(self):
        """Testa cálculo de porcentagem"""
        self.attempt.score = 8
        self.attempt.max_score = 10
        self.assertEqual(self.attempt.get_score_percentage(), 80.0)

    def test_attempt_get_score_percentage_zero_max(self):
        """Testa porcentagem com max_score zero"""
        self.attempt.score = 0
        self.attempt.max_score = 0
        self.assertEqual(self.attempt.get_score_percentage(), 0)

    def test_attempt_get_duration(self):
        """Testa cálculo de duração"""
        self.attempt.completed_at = self.attempt.started_at + timezone.timedelta(minutes=5)
        duration = self.attempt.get_duration()
        self.assertEqual(duration, 300)  # 5 minutos = 300 segundos

    def test_attempt_get_duration_not_completed(self):
        """Testa duração quando não completado"""
        self.assertIsNone(self.attempt.get_duration())

    def test_attempt_get_duration_formatted_seconds(self):
        """Testa formatação de duração em segundos"""
        self.attempt.completed_at = self.attempt.started_at + timezone.timedelta(seconds=45)
        self.assertEqual(self.attempt.get_duration_formatted(), "45s")

    def test_attempt_get_duration_formatted_minutes(self):
        """Testa formatação com minutos"""
        self.attempt.completed_at = self.attempt.started_at + timezone.timedelta(minutes=5, seconds=32)
        self.assertEqual(self.attempt.get_duration_formatted(), "5min 32s")

    def test_attempt_get_duration_formatted_hours(self):
        """Testa formatação com horas"""
        self.attempt.completed_at = self.attempt.started_at + timezone.timedelta(hours=1, minutes=23)
        self.assertEqual(self.attempt.get_duration_formatted(), "1h 23min")

    def test_attempt_initialize_question_order(self):
        """Testa inicialização da ordem"""
        self.assertIsNotNone(self.attempt.question_order)
        self.assertEqual(len(self.attempt.question_order), 10)
        self.assertEqual(self.attempt.max_score, 10)

    def test_attempt_initialize_question_order_with_sampling(self):
        """Testa sampling de questões"""
        quiz, questions = QuizFactory.create_with_questions(num_questions=20)
        quiz.question_sample_size = 10
        quiz.save()

        attempt = QuizAttemptFactory.create(quiz=quiz)
        self.assertEqual(len(attempt.question_order), 10)
        self.assertEqual(attempt.max_score, 10)

    def test_attempt_get_ordered_questions(self):
        """Testa obtenção de questões ordenadas"""
        questions = self.attempt.get_ordered_questions()
        self.assertEqual(len(questions), 10)

        # Verificar que a ordem corresponde
        for i, q in enumerate(questions):
            self.assertEqual(str(q.id), self.attempt.question_order[i])

    def test_attempt_for_anonymous_user(self):
        """Testa tentativa de usuário anônimo"""
        # Criar quiz sem user na factory
        from quizzes.models import QuizAttempt
        attempt = QuizAttempt.objects.create(
            user=None,
            quiz=self.quiz,
            session_key="anonymous_session_123",
            ip_address="127.0.0.1"
        )
        attempt.initialize_question_order()

        self.assertIsNone(attempt.user)
        self.assertEqual(attempt.session_key, "anonymous_session_123")


class UserAnswerModelTest(TestCase):
    """Testes para UserAnswer"""

    def setUp(self):
        self.user = UserFactory.create()
        self.quiz, self.questions = QuizFactory.create_with_questions(num_questions=5)
        self.attempt = QuizAttemptFactory.create(user=self.user, quiz=self.quiz)
        self.question = self.questions[0]
        self.correct_answer = self.question.get_correct_answer()

    def test_user_answer_creation(self):
        """Testa criação básica"""
        user_answer = UserAnswerFactory.create(
            attempt=self.attempt,
            question=self.question,
            selected_answer=self.correct_answer
        )
        self.assertIsNotNone(user_answer.id)
        self.assertEqual(user_answer.attempt, self.attempt)
        self.assertEqual(user_answer.question, self.question)

    def test_user_answer_auto_set_is_correct(self):
        """Testa que is_correct é setado automaticamente"""
        # Resposta correta
        correct_ua = UserAnswerFactory.create(
            attempt=self.attempt,
            question=self.question,
            selected_answer=self.correct_answer
        )
        self.assertTrue(correct_ua.is_correct)

        # Resposta incorreta
        wrong_answer = self.question.answers.filter(is_correct=False).first()
        wrong_ua = UserAnswerFactory.create(
            attempt=self.attempt,
            question=self.questions[1],
            selected_answer=wrong_answer
        )
        self.assertFalse(wrong_ua.is_correct)

    def test_user_answer_str_representation(self):
        """Testa string representation"""
        user_answer = UserAnswerFactory.create(
            attempt=self.attempt,
            question=self.question,
            selected_answer=self.correct_answer
        )
        str_repr = str(user_answer)
        self.assertIn("✓", str_repr)

    def test_user_answer_unique_together(self):
        """Testa constraint unique_together"""
        from django.db import IntegrityError

        UserAnswerFactory.create(
            attempt=self.attempt,
            question=self.question,
            selected_answer=self.correct_answer
        )

        with self.assertRaises(IntegrityError):
            UserAnswerFactory.create(
                attempt=self.attempt,
                question=self.question,  # Mesma questão
                selected_answer=self.correct_answer
            )

    def test_user_answer_update_existing(self):
        """Testa atualização de resposta existente"""
        # Primeira resposta
        ua = UserAnswerFactory.create(
            attempt=self.attempt,
            question=self.question,
            selected_answer=self.correct_answer
        )
        self.assertTrue(ua.is_correct)

        # Atualizar para resposta errada
        wrong_answer = self.question.answers.filter(is_correct=False).first()
        ua.selected_answer = wrong_answer
        ua.save()

        # Recarregar do banco
        ua.refresh_from_db()
        self.assertFalse(ua.is_correct)

    def test_user_answer_answered_at(self):
        """Testa timestamp automático"""
        ua = UserAnswerFactory.create(
            attempt=self.attempt,
            question=self.question,
            selected_answer=self.correct_answer
        )
        self.assertIsNotNone(ua.answered_at)

    def test_user_answer_cascade_delete(self):
        """Testa deleção em cascata"""
        ua = UserAnswerFactory.create(
            attempt=self.attempt,
            question=self.question,
            selected_answer=self.correct_answer
        )
        ua_id = ua.id

        self.attempt.delete()
        self.assertFalse(UserAnswer.objects.filter(id=ua_id).exists())
