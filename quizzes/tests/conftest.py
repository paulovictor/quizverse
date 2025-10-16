"""
Pytest configuration and fixtures
"""
import pytest
from django.test import Client
from quizzes.tests.fixtures.factories import (
    UserFactory, ThemeFactory, QuizFactory,
    QuestionFactory, AnswerFactory, BadgeFactory,
    QuizGroupFactory, QuizAttemptFactory
)


@pytest.fixture
def client():
    """Django test client"""
    return Client()


@pytest.fixture
def user():
    """Create a test user"""
    return UserFactory.create()


@pytest.fixture
def superuser():
    """Create a superuser"""
    return UserFactory.create_superuser()


@pytest.fixture
def theme():
    """Create a test theme"""
    return ThemeFactory.create()


@pytest.fixture
def quiz_group():
    """Create a quiz group"""
    return QuizGroupFactory.create()


@pytest.fixture
def quiz(theme, quiz_group):
    """Create a quiz with questions"""
    quiz, questions = QuizFactory.create_with_questions(
        theme=theme,
        quiz_group=quiz_group,
        num_questions=5
    )
    return quiz


@pytest.fixture
def quiz_attempt(user, quiz):
    """Create a quiz attempt"""
    return QuizAttemptFactory.create(user=user, quiz=quiz)


@pytest.fixture
def badge():
    """Create a badge"""
    return BadgeFactory.create()


@pytest.fixture
def authenticated_client(client, user):
    """Client with authenticated user"""
    client.force_login(user)
    return client
