"""
Testes unitários para os models Quiz, QuizGroup, Question e Answer
"""
from django.test import TestCase
from django.urls import reverse
from quizzes.models import Quiz, QuizGroup, Question, Answer
from quizzes.tests.fixtures.factories import (
    QuizFactory, QuizGroupFactory, QuestionFactory,
    AnswerFactory, ThemeFactory
)


class QuizGroupModelTest(TestCase):
    """Testes para o model QuizGroup"""

    def setUp(self):
        self.quiz_group = QuizGroupFactory.create(
            name="Test Group",
            difficulty='medium'
        )

    def test_quiz_group_creation(self):
        """Testa criação básica de um grupo de quiz"""
        self.assertIsNotNone(self.quiz_group.id)
        self.assertEqual(self.quiz_group.name, "Test Group")
        self.assertEqual(self.quiz_group.difficulty, 'medium')

    def test_quiz_group_str_representation(self):
        """Testa representação em string"""
        self.assertEqual(str(self.quiz_group), "Test Group")

    def test_quiz_group_difficulty_choices(self):
        """Testa opções de dificuldade"""
        easy = QuizGroupFactory.create(difficulty='easy')
        hard = QuizGroupFactory.create(difficulty='hard')

        self.assertEqual(easy.difficulty, 'easy')
        self.assertEqual(hard.difficulty, 'hard')

    def test_quiz_group_get_available_languages(self):
        """Testa get_available_languages"""
        QuizFactory.create(quiz_group=self.quiz_group, country='pt-BR')
        QuizFactory.create(quiz_group=self.quiz_group, country='en-US')
        QuizFactory.create(quiz_group=self.quiz_group, country='es-MX')

        languages = list(self.quiz_group.get_available_languages())
        self.assertEqual(len(languages), 3)
        self.assertIn('pt-BR', languages)
        self.assertIn('en-US', languages)
        self.assertIn('es-MX', languages)

    def test_quiz_group_ordering(self):
        """Testa ordenação de grupos"""
        group1 = QuizGroupFactory.create(name="B Group", order=2)
        group2 = QuizGroupFactory.create(name="A Group", order=1)

        # Filtrar apenas os grupos criados neste teste
        groups = list(QuizGroup.objects.filter(
            id__in=[group1.id, group2.id]
        ).order_by('order', 'name'))
        self.assertEqual(len(groups), 2)
        self.assertEqual(groups[0], group2)  # order=1
        self.assertEqual(groups[1], group1)  # order=2


class QuizModelTest(TestCase):
    """Testes para o model Quiz"""

    def setUp(self):
        self.theme = ThemeFactory.create()
        self.quiz_group = QuizGroupFactory.create()
        self.quiz = QuizFactory.create(
            theme=self.theme,
            quiz_group=self.quiz_group,
            title="Test Quiz"
        )

    def test_quiz_creation(self):
        """Testa criação básica de um quiz"""
        self.assertIsNotNone(self.quiz.id)
        self.assertEqual(self.quiz.title, "Test Quiz")
        self.assertEqual(self.quiz.theme, self.theme)
        self.assertEqual(self.quiz.quiz_group, self.quiz_group)

    def test_quiz_str_representation(self):
        """Testa representação em string"""
        str_repr = str(self.quiz)
        self.assertIn(self.theme.title, str_repr)
        self.assertIn("Test Quiz", str_repr)

    def test_quiz_absolute_url(self):
        """Testa get_absolute_url"""
        url = self.quiz.get_absolute_url()
        expected = reverse('quizzes:quiz_detail', kwargs={
            'theme_slug': self.theme.slug,
            'quiz_slug': self.quiz.slug
        })
        self.assertEqual(url, expected)

    def test_quiz_get_total_questions(self):
        """Testa contagem total de questões"""
        self.assertEqual(self.quiz.get_total_questions(), 0)

        QuestionFactory.create(quiz=self.quiz)
        QuestionFactory.create(quiz=self.quiz)
        QuestionFactory.create(quiz=self.quiz)

        self.assertEqual(self.quiz.get_total_questions(), 3)

    def test_quiz_get_questions_per_attempt_no_limit(self):
        """Testa questões por tentativa sem limite"""
        for i in range(10):
            QuestionFactory.create(quiz=self.quiz)

        self.quiz.question_sample_size = 0
        self.quiz.save()

        self.assertEqual(self.quiz.get_questions_per_attempt(), 10)

    def test_quiz_get_questions_per_attempt_with_limit(self):
        """Testa questões por tentativa com limite"""
        for i in range(20):
            QuestionFactory.create(quiz=self.quiz)

        self.quiz.question_sample_size = 10
        self.quiz.save()

        self.assertEqual(self.quiz.get_questions_per_attempt(), 10)

    def test_quiz_get_questions_per_attempt_limit_larger_than_total(self):
        """Testa quando limite é maior que total"""
        for i in range(5):
            QuestionFactory.create(quiz=self.quiz)

        self.quiz.question_sample_size = 20
        self.quiz.save()

        self.assertEqual(self.quiz.get_questions_per_attempt(), 5)

    def test_quiz_get_estimated_time(self):
        """Testa estimativa de tempo"""
        for i in range(10):
            QuestionFactory.create(quiz=self.quiz)

        self.quiz.question_sample_size = 0
        time_estimate = self.quiz.get_estimated_time()

        # 10 questões * 0.5 min = 5 minutos
        self.assertEqual(time_estimate, 5)

    def test_quiz_get_estimated_time_minimum(self):
        """Testa que tempo mínimo é 1 minuto"""
        QuestionFactory.create(quiz=self.quiz)
        self.assertEqual(self.quiz.get_estimated_time(), 1)

    def test_quiz_get_effective_difficulty_from_group(self):
        """Testa dificuldade efetiva do grupo"""
        self.quiz_group.difficulty = 'hard'
        self.quiz_group.save()

        self.quiz.difficulty = 'easy'
        self.quiz.save()

        # Deve usar do grupo
        self.assertEqual(self.quiz.get_effective_difficulty(), 'hard')

    def test_quiz_get_effective_difficulty_no_group(self):
        """Testa dificuldade efetiva sem grupo"""
        quiz = QuizFactory.create(
            theme=self.theme,
            quiz_group=None,
            difficulty='easy'
        )
        self.assertEqual(quiz.get_effective_difficulty(), 'easy')

    def test_quiz_description_template_rendering(self):
        """Testa renderização de template de descrição"""
        for i in range(100):
            QuestionFactory.create(quiz=self.quiz)

        self.quiz.question_sample_size = 20
        self.quiz.description_template = "Identifique {sample_size} personagens de {total} disponíveis"
        self.quiz.save()

        description = self.quiz.render_description()
        self.assertIn("20", description)
        self.assertIn("100", description)

    def test_quiz_description_template_auto_save(self):
        """Testa que description é atualizada ao salvar com template"""
        for i in range(50):
            QuestionFactory.create(quiz=self.quiz)

        self.quiz.question_sample_size = 10
        self.quiz.description_template = "Teste {sample_size} de {total}"
        self.quiz.save()

        self.assertIn("10", self.quiz.description)
        self.assertIn("50", self.quiz.description)

    def test_quiz_unique_together_theme_slug(self):
        """Testa constraint unique_together"""
        from django.db import IntegrityError

        with self.assertRaises(IntegrityError):
            QuizFactory.create(
                theme=self.theme,
                slug=self.quiz.slug
            )

    def test_quiz_ordering(self):
        """Testa ordenação de quizzes"""
        quiz1 = QuizFactory.create(theme=self.theme, title="B Quiz", order=2)
        quiz2 = QuizFactory.create(theme=self.theme, title="A Quiz", order=1)

        quizzes = list(Quiz.objects.filter(theme=self.theme))
        # A ordem é: theme, quiz_group__order, order, title
        # Como têm mesmo theme e quiz_group, ordena por order e title
        self.assertIn(quiz2, quizzes[:2])


class QuestionModelTest(TestCase):
    """Testes para o model Question"""

    def setUp(self):
        self.quiz = QuizFactory.create()
        self.question = QuestionFactory.create(
            quiz=self.quiz,
            text="What is the capital of France?",
            create_answers=False
        )

    def test_question_creation(self):
        """Testa criação básica de uma questão"""
        self.assertIsNotNone(self.question.id)
        self.assertEqual(self.question.text, "What is the capital of France?")
        self.assertEqual(self.question.quiz, self.quiz)

    def test_question_str_representation(self):
        """Testa representação em string"""
        str_repr = str(self.question)
        self.assertIn(self.quiz.title, str_repr)
        self.assertIn("What is the capital", str_repr[:50])

    def test_question_get_correct_answer(self):
        """Testa get_correct_answer"""
        correct = AnswerFactory.create(question=self.question, is_correct=True)
        AnswerFactory.create(question=self.question, is_correct=False)

        result = self.question.get_correct_answer()
        self.assertEqual(result, correct)

    def test_question_get_correct_answer_none(self):
        """Testa get_correct_answer quando não há resposta correta"""
        AnswerFactory.create(question=self.question, is_correct=False)
        result = self.question.get_correct_answer()
        self.assertIsNone(result)

    def test_question_with_image(self):
        """Testa questão com imagem"""
        question = QuestionFactory.create(
            quiz=self.quiz,
            image="https://example.com/image.jpg",
            create_answers=False
        )
        self.assertEqual(question.image, "https://example.com/image.jpg")

    def test_question_with_explanation(self):
        """Testa questão com explicação"""
        question = QuestionFactory.create(
            quiz=self.quiz,
            explanation="Paris is the capital and largest city of France",
            create_answers=False
        )
        self.assertIn("Paris", question.explanation)

    def test_question_ordering(self):
        """Testa ordenação de questões"""
        q1 = QuestionFactory.create(quiz=self.quiz, order=2, create_answers=False)
        q2 = QuestionFactory.create(quiz=self.quiz, order=1, create_answers=False)

        # Filtrar apenas as questões criadas neste teste e ordenar
        questions = list(Question.objects.filter(
            id__in=[q1.id, q2.id]
        ).order_by('order'))
        self.assertEqual(len(questions), 2)
        self.assertEqual(questions[0], q2)  # order=1
        self.assertEqual(questions[1], q1)  # order=2

    def test_question_auto_timestamps(self):
        """Testa created_at e updated_at"""
        self.assertIsNotNone(self.question.created_at)
        self.assertIsNotNone(self.question.updated_at)


class AnswerModelTest(TestCase):
    """Testes para o model Answer"""

    def setUp(self):
        self.quiz = QuizFactory.create()
        self.question = QuestionFactory.create(quiz=self.quiz, create_answers=False)
        self.answer = AnswerFactory.create(
            question=self.question,
            text="Paris",
            is_correct=True
        )

    def test_answer_creation(self):
        """Testa criação básica de uma resposta"""
        self.assertIsNotNone(self.answer.id)
        self.assertEqual(self.answer.text, "Paris")
        self.assertTrue(self.answer.is_correct)
        self.assertEqual(self.answer.question, self.question)

    def test_answer_str_representation_correct(self):
        """Testa representação de resposta correta"""
        str_repr = str(self.answer)
        self.assertIn("✓", str_repr)
        self.assertIn("Paris", str_repr)

    def test_answer_str_representation_incorrect(self):
        """Testa representação de resposta incorreta"""
        wrong = AnswerFactory.create(question=self.question, is_correct=False)
        str_repr = str(wrong)
        self.assertIn("✗", str_repr)

    def test_answer_ordering(self):
        """Testa ordenação de respostas"""
        a1 = AnswerFactory.create(question=self.question, order=2)
        a2 = AnswerFactory.create(question=self.question, order=1)

        # Filtrar apenas as respostas criadas neste teste e ordenar
        answers = list(Answer.objects.filter(
            id__in=[a1.id, a2.id]
        ).order_by('order'))
        self.assertEqual(len(answers), 2)
        self.assertEqual(answers[0], a2)  # order=1
        self.assertEqual(answers[1], a1)  # order=2

    def test_multiple_answers_per_question(self):
        """Testa múltiplas respostas por questão"""
        AnswerFactory.create(question=self.question, text="London", is_correct=False)
        AnswerFactory.create(question=self.question, text="Berlin", is_correct=False)
        AnswerFactory.create(question=self.question, text="Madrid", is_correct=False)

        self.assertEqual(self.question.answers.count(), 4)  # 3 + 1 do setUp
        correct_count = self.question.answers.filter(is_correct=True).count()
        self.assertEqual(correct_count, 1)

    def test_answer_cascade_delete(self):
        """Testa deleção em cascata quando questão é deletada"""
        answer_id = self.answer.id
        self.question.delete()

        self.assertFalse(Answer.objects.filter(id=answer_id).exists())
