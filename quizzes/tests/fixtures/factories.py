"""
Test Factories using Factory Boy pattern
Fornece objetos de teste configuráveis e reutilizáveis
"""
from django.contrib.auth.models import User
from quizzes.models import (
    Theme, Quiz, QuizGroup, Question, Answer,
    QuizAttempt, UserAnswer, Badge, QuizGroupBadge, UserBadge, Product
)
from decimal import Decimal
import uuid


class BaseFactory:
    """Base factory com métodos comuns"""

    @staticmethod
    def create_unique_slug(prefix=""):
        """Gera slug único usando UUID"""
        return f"{prefix}{uuid.uuid4().hex[:8]}"


class UserFactory(BaseFactory):
    """Factory para User"""

    @staticmethod
    def create(username=None, email=None, password="testpass123", **kwargs):
        """Cria um usuário para testes"""
        if not username:
            username = f"user_{uuid.uuid4().hex[:8]}"
        if not email:
            email = f"{username}@test.com"

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            **kwargs
        )
        return user

    @staticmethod
    def create_superuser(**kwargs):
        """Cria um superusuário"""
        username = kwargs.pop('username', f"admin_{uuid.uuid4().hex[:8]}")
        return User.objects.create_superuser(
            username=username,
            email=f"{username}@test.com",
            password="adminpass123",
            **kwargs
        )


class ThemeFactory(BaseFactory):
    """Factory para Theme"""

    @staticmethod
    def create(title=None, parent=None, country='pt-BR', **kwargs):
        """Cria um tema"""
        if not title:
            title = f"Theme {uuid.uuid4().hex[:8]}"

        slug = kwargs.pop('slug', None) or ThemeFactory.create_unique_slug("theme-")

        return Theme.objects.create(
            title=title,
            description=kwargs.pop('description', f"Description for {title}"),
            slug=slug,
            parent=parent,
            country=country,
            active=kwargs.pop('active', True),
            order=kwargs.pop('order', 0),
            **kwargs
        )

    @staticmethod
    def create_with_subcategories(num_subcategories=2, country='pt-BR'):
        """Cria um tema com subcategorias"""
        parent = ThemeFactory.create(title="Parent Theme", country=country)
        subcategories = [
            ThemeFactory.create(
                title=f"Subcategory {i+1}",
                parent=parent,
                country=country
            )
            for i in range(num_subcategories)
        ]
        return parent, subcategories


class QuizGroupFactory(BaseFactory):
    """Factory para QuizGroup"""

    @staticmethod
    def create(name=None, difficulty='medium', **kwargs):
        """Cria um grupo de quiz"""
        if not name:
            name = f"Quiz Group {uuid.uuid4().hex[:8]}"

        slug = kwargs.pop('slug', None) or QuizGroupFactory.create_unique_slug("group-")

        return QuizGroup.objects.create(
            name=name,
            slug=slug,
            difficulty=difficulty,
            description=kwargs.pop('description', f"Description for {name}"),
            order=kwargs.pop('order', 0),
            **kwargs
        )


class QuizFactory(BaseFactory):
    """Factory para Quiz"""

    @staticmethod
    def create(theme=None, quiz_group=None, title=None, country='pt-BR', **kwargs):
        """Cria um quiz"""
        if not theme:
            theme = ThemeFactory.create(country=country)

        if not title:
            title = f"Quiz {uuid.uuid4().hex[:8]}"

        slug = kwargs.pop('slug', None) or QuizFactory.create_unique_slug("quiz-")

        return Quiz.objects.create(
            theme=theme,
            quiz_group=quiz_group,
            title=title,
            slug=slug,
            description=kwargs.pop('description', f"Description for {title}"),
            difficulty=kwargs.pop('difficulty', 'medium'),
            country=country,
            time_limit=kwargs.pop('time_limit', 0),
            question_sample_size=kwargs.pop('question_sample_size', 0),
            active=kwargs.pop('active', True),
            order=kwargs.pop('order', 0),
            **kwargs
        )

    @staticmethod
    def create_with_questions(theme=None, num_questions=5, **kwargs):
        """Cria um quiz com questões"""
        quiz = QuizFactory.create(theme=theme, **kwargs)
        questions = [
            QuestionFactory.create(quiz=quiz, order=i)
            for i in range(num_questions)
        ]
        return quiz, questions


class QuestionFactory(BaseFactory):
    """Factory para Question"""

    @staticmethod
    def create(quiz=None, text=None, order=0, **kwargs):
        """Cria uma questão"""
        if not quiz:
            quiz = QuizFactory.create()

        if not text:
            text = f"Question {uuid.uuid4().hex[:8]}"

        # Remover create_answers dos kwargs antes de criar
        create_answers = kwargs.pop('create_answers', True)

        question = Question.objects.create(
            quiz=quiz,
            text=text,
            order=order,
            image=kwargs.pop('image', None),
            explanation=kwargs.pop('explanation', ''),
            **kwargs
        )

        # Criar 4 respostas por padrão (1 correta, 3 incorretas)
        if create_answers:
            AnswerFactory.create(question=question, text="Correct Answer", is_correct=True, order=0)
            for i in range(3):
                AnswerFactory.create(question=question, text=f"Wrong Answer {i+1}", is_correct=False, order=i+1)

        return question


class AnswerFactory(BaseFactory):
    """Factory para Answer"""

    @staticmethod
    def create(question=None, text=None, is_correct=False, order=0, **kwargs):
        """Cria uma resposta"""
        if not question:
            quiz = QuizFactory.create()
            question = QuestionFactory.create(quiz=quiz, create_answers=False)

        if not text:
            text = f"Answer {uuid.uuid4().hex[:8]}"

        return Answer.objects.create(
            question=question,
            text=text,
            is_correct=is_correct,
            order=order,
            **kwargs
        )


class QuizAttemptFactory(BaseFactory):
    """Factory para QuizAttempt"""

    @staticmethod
    def create(user=None, quiz=None, completed=False, score=None, **kwargs):
        """Cria uma tentativa de quiz"""
        if not user:
            user = UserFactory.create()

        if not quiz:
            quiz, questions = QuizFactory.create_with_questions()

        attempt = QuizAttempt.objects.create(
            user=user,
            quiz=quiz,
            session_key=kwargs.pop('session_key', 'test_session'),
            ip_address=kwargs.pop('ip_address', '127.0.0.1'),
            score=score if score is not None else 0,
            max_score=kwargs.pop('max_score', 0),
            **kwargs
        )

        # Inicializar ordem das questões
        if not attempt.question_order:
            attempt.initialize_question_order()

        # Se completado, adicionar completed_at
        if completed:
            from django.utils import timezone
            attempt.completed_at = timezone.now()
            if score is None:
                attempt.score = attempt.max_score // 2  # 50% por padrão
            attempt.save()

        return attempt

    @staticmethod
    def create_with_answers(user=None, quiz=None, num_correct=None, **kwargs):
        """Cria uma tentativa com respostas"""
        if not quiz:
            quiz, questions = QuizFactory.create_with_questions(num_questions=10)
        else:
            questions = list(quiz.questions.all())

        attempt = QuizAttemptFactory.create(user=user, quiz=quiz, **kwargs)
        attempt.initialize_question_order()

        # Determinar quantas corretas
        if num_correct is None:
            num_correct = len(questions) // 2

        # Criar respostas
        for i, question in enumerate(questions):
            is_correct = i < num_correct
            correct_answer = question.get_correct_answer()
            wrong_answers = question.answers.filter(is_correct=False)

            selected = correct_answer if is_correct else wrong_answers.first()
            UserAnswerFactory.create(
                attempt=attempt,
                question=question,
                selected_answer=selected
            )

        # Atualizar score
        attempt.score = num_correct
        attempt.max_score = len(questions)
        attempt.save()

        return attempt, questions


class UserAnswerFactory(BaseFactory):
    """Factory para UserAnswer"""

    @staticmethod
    def create(attempt=None, question=None, selected_answer=None, **kwargs):
        """Cria uma resposta de usuário"""
        if not attempt:
            attempt = QuizAttemptFactory.create()

        if not question:
            question = QuestionFactory.create(quiz=attempt.quiz)

        if not selected_answer:
            selected_answer = question.get_correct_answer()

        return UserAnswer.objects.create(
            attempt=attempt,
            question=question,
            selected_answer=selected_answer,
            **kwargs
        )


class BadgeFactory(BaseFactory):
    """Factory para Badge"""

    @staticmethod
    def create(title=None, rule_type='percentage', min_percentage=80, **kwargs):
        """Cria uma badge"""
        if not title:
            title = f"Badge {uuid.uuid4().hex[:8]}"

        return Badge.objects.create(
            title=title,
            description=kwargs.pop('description', f"Description for {title}"),
            image=kwargs.pop('image', "https://via.placeholder.com/150"),
            rule_type=rule_type,
            min_percentage=Decimal(str(min_percentage)),
            max_time_seconds=kwargs.pop('max_time_seconds', None),
            rarity=kwargs.pop('rarity', 'common'),
            points=kwargs.pop('points', 10),
            order=kwargs.pop('order', 0),
            active=kwargs.pop('active', True),
            description_translations=kwargs.pop('description_translations', {}),
            **kwargs
        )


class QuizGroupBadgeFactory(BaseFactory):
    """Factory para QuizGroupBadge"""

    @staticmethod
    def create(quiz_group=None, badge=None, **kwargs):
        """Associa badge a grupo"""
        if not quiz_group:
            quiz_group = QuizGroupFactory.create()

        if not badge:
            badge = BadgeFactory.create()

        return QuizGroupBadge.objects.create(
            quiz_group=quiz_group,
            badge=badge,
            active=kwargs.pop('active', True),
            **kwargs
        )


class UserBadgeFactory(BaseFactory):
    """Factory para UserBadge"""

    @staticmethod
    def create(user=None, badge=None, quiz_group=None, quiz_attempt=None, **kwargs):
        """Cria uma badge conquistada"""
        if not user:
            user = UserFactory.create()

        if not quiz_group:
            quiz_group = QuizGroupFactory.create()

        if not badge:
            badge = BadgeFactory.create()
            # Associar badge ao grupo
            QuizGroupBadgeFactory.create(quiz_group=quiz_group, badge=badge)

        if not quiz_attempt:
            quiz = QuizFactory.create(quiz_group=quiz_group)
            quiz_attempt = QuizAttemptFactory.create(user=user, quiz=quiz, completed=True)

        return UserBadge.objects.create(
            user=user,
            badge=badge,
            quiz_group=quiz_group,
            quiz_attempt=quiz_attempt,
            score_percentage=kwargs.pop('score_percentage', Decimal('85.0')),
            completion_time_seconds=kwargs.pop('completion_time_seconds', 120),
            **kwargs
        )


class ProductFactory(BaseFactory):
    """Factory para Product"""

    @staticmethod
    def create(theme=None, title=None, **kwargs):
        """Cria um produto"""
        if not theme:
            theme = ThemeFactory.create()

        if not title:
            title = f"Product {uuid.uuid4().hex[:8]}"

        return Product.objects.create(
            theme=theme,
            title=title,
            price=kwargs.pop('price', Decimal('99.99')),
            discount_percentage=kwargs.pop('discount_percentage', 0),
            image_url=kwargs.pop('image_url', "https://via.placeholder.com/300"),
            product_url=kwargs.pop('product_url', "https://example.com/product"),
            active=kwargs.pop('active', True),
            order=kwargs.pop('order', 0),
            **kwargs
        )
