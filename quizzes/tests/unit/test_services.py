"""
Testes unitários para services.py
"""
from django.test import TestCase
from decimal import Decimal
from quizzes import services
from quizzes.tests.fixtures.factories import (
    UserFactory, QuizFactory, QuizGroupFactory,
    QuizAttemptFactory, BadgeFactory, QuizGroupBadgeFactory
)


class BadgeServicesTest(TestCase):
    """Testes para funções de badge em services"""

    def setUp(self):
        self.user = UserFactory.create()
        self.quiz_group = QuizGroupFactory.create()
        self.quiz = QuizFactory.create(quiz_group=self.quiz_group)

        # Criar badges
        self.badge_80 = BadgeFactory.create(
            title="80% Badge",
            rule_type='percentage',
            min_percentage=80
        )
        self.badge_perfect = BadgeFactory.create(
            title="Perfect Badge",
            rule_type='perfect_score'
        )

        # Associar ao grupo
        QuizGroupBadgeFactory.create(quiz_group=self.quiz_group, badge=self.badge_80)
        QuizGroupBadgeFactory.create(quiz_group=self.quiz_group, badge=self.badge_perfect)

    def test_badge_criteria_met_percentage(self):
        """Testa critério de porcentagem"""
        # Criar quiz com 10 questões
        quiz, _ = QuizFactory.create_with_questions(
            quiz_group=self.quiz_group,
            num_questions=10
        )

        attempt, _ = QuizAttemptFactory.create_with_answers(
            user=self.user,
            quiz=quiz,
            num_correct=8  # 80%
        )

        from django.utils import timezone
        attempt.completed_at = timezone.now()
        attempt.save()

        result = services.badge_criteria_met(attempt, self.badge_80)
        self.assertTrue(result)

    def test_badge_criteria_not_met_percentage(self):
        """Testa quando não atinge porcentagem"""
        # Criar quiz com 10 questões
        quiz, _ = QuizFactory.create_with_questions(
            quiz_group=self.quiz_group,
            num_questions=10
        )

        attempt, _ = QuizAttemptFactory.create_with_answers(
            user=self.user,
            quiz=quiz,
            num_correct=7  # 70%
        )

        from django.utils import timezone
        attempt.completed_at = timezone.now()
        attempt.save()

        result = services.badge_criteria_met(attempt, self.badge_80)
        self.assertFalse(result)

    def test_badge_criteria_met_perfect_score(self):
        """Testa critério de pontuação perfeita"""
        # Criar quiz com 10 questões
        quiz, questions = QuizFactory.create_with_questions(
            quiz_group=self.quiz_group,
            num_questions=10
        )

        attempt, _ = QuizAttemptFactory.create_with_answers(
            user=self.user,
            quiz=quiz,
            num_correct=len(questions)  # 100%
        )

        from django.utils import timezone
        attempt.completed_at = timezone.now()
        attempt.save()

        result = services.badge_criteria_met(attempt, self.badge_perfect)
        self.assertTrue(result)

    def test_check_and_award_badges_success(self):
        """Testa concessão de badges"""
        # Criar quiz com 10 questões
        quiz, _ = QuizFactory.create_with_questions(
            quiz_group=self.quiz_group,
            num_questions=10
        )

        attempt, _ = QuizAttemptFactory.create_with_answers(
            user=self.user,
            quiz=quiz,
            num_correct=8  # 80%
        )

        from django.utils import timezone
        attempt.completed_at = timezone.now()
        attempt.save()

        new_badges = services.check_and_award_badges(attempt)
        self.assertEqual(len(new_badges), 1)
        self.assertEqual(new_badges[0].badge, self.badge_80)

    def test_check_and_award_badges_no_duplicate(self):
        """Testa que não concede badges duplicadas"""
        # Criar quiz com 10 questões
        quiz, _ = QuizFactory.create_with_questions(
            quiz_group=self.quiz_group,
            num_questions=10
        )

        attempt, _ = QuizAttemptFactory.create_with_answers(
            user=self.user,
            quiz=quiz,
            num_correct=8
        )

        from django.utils import timezone
        attempt.completed_at = timezone.now()
        attempt.save()

        # Primeira vez
        new_badges1 = services.check_and_award_badges(attempt)
        self.assertEqual(len(new_badges1), 1)

        # Segunda tentativa com mesma performance
        attempt2, _ = QuizAttemptFactory.create_with_answers(
            user=self.user,
            quiz=quiz,
            num_correct=8
        )
        attempt2.completed_at = timezone.now()
        attempt2.save()

        new_badges2 = services.check_and_award_badges(attempt2)
        self.assertEqual(len(new_badges2), 0)  # Já tem essa badge

    def test_get_user_badges_for_group(self):
        """Testa busca de badges do usuário em um grupo"""
        # Criar quiz com 10 questões
        quiz, _ = QuizFactory.create_with_questions(
            quiz_group=self.quiz_group,
            num_questions=10
        )

        attempt, _ = QuizAttemptFactory.create_with_answers(
            user=self.user,
            quiz=quiz,
            num_correct=8
        )

        from django.utils import timezone
        attempt.completed_at = timezone.now()
        attempt.save()

        services.check_and_award_badges(attempt)

        user_badges = services.get_user_badges_for_group(self.user, self.quiz_group)
        self.assertEqual(user_badges.count(), 1)

    def test_get_available_badges_for_group(self):
        """Testa busca de badges disponíveis"""
        badges = services.get_available_badges_for_group(self.quiz_group)
        self.assertEqual(badges.count(), 2)

    def test_get_user_badge_progress(self):
        """Testa progresso do usuário"""
        # Criar quiz com 10 questões
        quiz, _ = QuizFactory.create_with_questions(
            quiz_group=self.quiz_group,
            num_questions=10
        )

        attempt, _ = QuizAttemptFactory.create_with_answers(
            user=self.user,
            quiz=quiz,
            num_correct=8
        )

        from django.utils import timezone
        attempt.completed_at = timezone.now()
        attempt.save()

        services.check_and_award_badges(attempt)

        progress = services.get_user_badge_progress(self.user, self.quiz_group)
        self.assertEqual(progress['total'], 2)
        self.assertEqual(progress['earned'], 1)
        self.assertEqual(progress['remaining'], 1)
        self.assertEqual(progress['percentage'], 50.0)
