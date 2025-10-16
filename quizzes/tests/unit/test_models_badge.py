"""
Testes unitários para Badge, QuizGroupBadge e UserBadge
"""
from django.test import TestCase
from decimal import Decimal
from quizzes.models import Badge, QuizGroupBadge, UserBadge
from quizzes.tests.fixtures.factories import (
    BadgeFactory, QuizGroupBadgeFactory, UserBadgeFactory,
    UserFactory, QuizGroupFactory, QuizAttemptFactory
)


class BadgeModelTest(TestCase):
    """Testes para Badge"""

    def test_badge_creation(self):
        badge = BadgeFactory.create(title="Test Badge", min_percentage=80)
        self.assertEqual(badge.title, "Test Badge")
        self.assertEqual(badge.min_percentage, Decimal('80'))

    def test_badge_get_description_with_translation(self):
        badge = BadgeFactory.create(
            description="Default description",
            description_translations={
                'pt-BR': 'Descrição em português',
                'en-US': 'Description in English'
            }
        )
        self.assertEqual(badge.get_description('pt-BR'), 'Descrição em português')
        self.assertEqual(badge.get_description('en-US'), 'Description in English')

    def test_badge_get_description_fallback(self):
        badge = BadgeFactory.create(description="Default description")
        self.assertEqual(badge.get_description('fr-FR'), 'Default description')

    def test_badge_rule_types(self):
        percentage_badge = BadgeFactory.create(rule_type='percentage')
        perfect_badge = BadgeFactory.create(rule_type='perfect_score')
        self.assertEqual(percentage_badge.rule_type, 'percentage')
        self.assertEqual(perfect_badge.rule_type, 'perfect_score')

    def test_badge_rarity_levels(self):
        common = BadgeFactory.create(rarity='common')
        legendary = BadgeFactory.create(rarity='legendary')
        self.assertEqual(common.rarity, 'common')
        self.assertEqual(legendary.rarity, 'legendary')


class QuizGroupBadgeModelTest(TestCase):
    """Testes para QuizGroupBadge"""

    def test_quiz_group_badge_creation(self):
        qgb = QuizGroupBadgeFactory.create()
        self.assertIsNotNone(qgb.id)
        self.assertTrue(qgb.active)

    def test_quiz_group_badge_unique_together(self):
        from django.db import IntegrityError
        quiz_group = QuizGroupFactory.create()
        badge = BadgeFactory.create()
        QuizGroupBadgeFactory.create(quiz_group=quiz_group, badge=badge)

        with self.assertRaises(IntegrityError):
            QuizGroupBadgeFactory.create(quiz_group=quiz_group, badge=badge)


class UserBadgeModelTest(TestCase):
    """Testes para UserBadge"""

    def setUp(self):
        self.user = UserFactory.create()
        self.quiz_group = QuizGroupFactory.create()
        self.badge = BadgeFactory.create()
        QuizGroupBadgeFactory.create(quiz_group=self.quiz_group, badge=self.badge)

    def test_user_badge_creation(self):
        ub = UserBadgeFactory.create(
            user=self.user,
            badge=self.badge,
            quiz_group=self.quiz_group
        )
        self.assertIsNotNone(ub.id)
        self.assertEqual(ub.user, self.user)
        self.assertEqual(ub.badge, self.badge)

    def test_user_badge_unique_together(self):
        from django.db import IntegrityError
        UserBadgeFactory.create(
            user=self.user,
            badge=self.badge,
            quiz_group=self.quiz_group
        )

        with self.assertRaises(IntegrityError):
            UserBadgeFactory.create(
                user=self.user,
                badge=self.badge,
                quiz_group=self.quiz_group
            )

    def test_user_badge_validation_badge_not_in_group(self):
        """Badge deve estar disponível no grupo"""
        other_badge = BadgeFactory.create()
        # Não associar ao grupo

        with self.assertRaises(ValueError):
            UserBadgeFactory.create(
                user=self.user,
                badge=other_badge,
                quiz_group=self.quiz_group
            )
