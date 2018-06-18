from django.test import TestCase
from .models import Quiz, QuizInstance, RoundCategory, QuizRound
from django.utils import timezone
from datetime import datetime

# Create your tests here.


def create_quiz(quiz_name, maximum_score, overall_record_score, personal_record_score, rounds):
    quiz = Quiz.objects.create(quiz_name=quiz_name, maximum_score=maximum_score,
                               overall_record_score=overall_record_score, personal_record_score=personal_record_score, rounds=rounds)
    return quiz


def create_quiz_instance(quiz_type, quiz_date, team_size, pints_consumed, number_of_teams, winning_score, teams_above_ninety, bonus_score):
    quiz_instance = QuizInstance.objects.create(quiz_type=quiz_type, quiz_date=quiz_date,
                                                team_size=team_size, pints_consumed=pints_consumed, number_of_teams=number_of_teams, winning_score=winning_score, teams_above_ninety=teams_above_ninety, bonus_score=bonus_score)
    return quiz_instance


def create_round_category(category):
    round_category = RoundCategory.objects.create(category=category)
    return round_category


def create_quiz_round(quiz_instance, round_number, category, score, doubler):
    quiz_round = QuizRound.objects.create(
        quiz_instance=quiz_instance, round_number=round_number, category=category, score=score, doubler=doubler)
    return quiz_round


class TestQuizModel(TestCase):
    pass


class TestQuizInstanceModel(TestCase):
    pass


class TestRoundCategory(TestCase):
    pass


class TestQuizRound(TestCase):
    pass
