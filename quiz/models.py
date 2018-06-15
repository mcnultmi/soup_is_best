from django.db import models

# Create your models here.

class Quiz(models.Model):
    """ Represents the general structure of a quiz """

    quiz_name = models.CharField(
        max_length=250,
        help_text="Name that can be used to identify a quiz"
        )
    overall_record_score = models.IntegerField(
        null=True,
        help_text="Highest score ever recorded at this quiz"
        )
    personal_record_score = models.IntegerField(
        null=True,
        help_text="Highest score that your team has scored at this quiz"
        )
    number_of_rounds = models.IntegerField(
        help_text="Number of standard rounds in the quiz"
    )

    class Meta:
        verbose_name_plural = "quizzes"


class QuizInstance(models.Model):
    """ Represents one occurrence of a particular quiz """

    quiz_name = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE
        )
    quiz_date = models.DateField()
    team_size = models.IntegerField()
    pints_consumed = models.IntegerField(
        null=True
        )
    number_of_teams = models.IntegerField(
        null=True,
        help_text="Number of teams competing"
        )
    top_score = models.IntegerField(
        help_text="Top score achieved by any one team"
        )
    teams_above_ninety = models.IntegerField(
        help_text="Number of teams that scored above 90 points"
        )
    bonus_score = models.IntegerField(
        help_text="Number of points scored on the bonus question"
        )


class RoundCategory(models.Model):
    """ Represents the category of a particular QuizRound """

    category = models.CharField(
        max_length=100
        )

    class Meta:
        verbose_name_plural = "round categories"

class QuizRound(models.Model):
    """ Represents a single round in the quiz """

    quiz_instance = models.ForeignKey(
        QuizInstance,
        on_delete=models.CASCADE
        )
    round_number = models.IntegerField()
    category = models.ForeignKey(
        RoundCategory,
        null=False,
        on_delete=models.PROTECT
        )
    score = models.IntegerField()
    doubler = models.BooleanField(
        default=False
        )