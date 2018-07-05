from django.contrib.auth import get_user_model
from ..models import QuizBase, QuizInstance, RoundCategory, QuizRound
from datetime import date
from django.test import TestCase
from django.utils import timezone


def create_user():
    """ Create a test user with pk=1 """
    return get_user_model().objects.create(pk=1, username='test_user')


def create_quiz():
    """ Create a test quiz, created by a user with pk=1 """
    user = create_user()
    return QuizBase.objects.create(create_by=user, quiz_name='Test Quiz')


def create_quiz_instance(quiz, quiz_date):
    """ Create a quiz instance for a chosen quiz and date """
    return QuizInstance.objects.create(quiz=quiz, quiz_date=quiz_date)


def create_round_category():
    return RoundCategory.objects.create(category='Alphabet Soup')


def create_quiz_round():
    quiz = create_quiz()
    quiz_instance = create_quiz_instance(
        quiz=quiz, quiz_date=timezone.now().date())
    category = create_round_category()
    return QuizRound.objects.create(quiz_instance=quiz_instance, category=category, round_number=1, score=10)


class TestQuizBaseModel(TestCase):

    def test_create_by_user(self):
        """ Test that create_by field is working correctly """
        quiz = create_quiz()
        user = get_user_model().objects.get(pk=1)
        self.assertEqual(user, quiz.create_by)
        self.assertEqual(user.pk, quiz.create_by.pk)

    def test_quiz_name(self):
        """ Test the __str__() method is correctly giving the quiz name """
        quiz = create_quiz()
        self.assertEqual(quiz.quiz_name, quiz.__str__())


class TestQuizInstanceModel(TestCase):

    def test_quiz_instance_name(self):
        """ Test the __str__() method is correctly giving the quiz name and date"""
        quiz = create_quiz()
        quiz_instance = create_quiz_instance(
            quiz=quiz, quiz_date=timezone.now().date())
        self.assertEquals(quiz_instance.quiz.quiz_name + ' (' +
                          quiz_instance.quiz_date.strftime('%d-%m-%Y') + ')', quiz_instance.__str__())


class TestRoundCategory(TestCase):

    def test_round_category_name(self):
        """ Test the __str__() method is just producing the category name """
        category = create_round_category()
        self.assertEqual(category.__str__(), category.category)


class TestQuizRound(TestCase):

    def test_quiz_round_name(self):
        """ Test the __str__() method is giving the quiz name, date and category """
        quiz_round = create_quiz_round()
        self.assertEqual(quiz_round.__str__(), 'Test Quiz (%s) - Alphabet Soup' %
                         timezone.now().date().strftime('%d-%m-%Y'))
