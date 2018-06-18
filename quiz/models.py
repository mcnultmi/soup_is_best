from django.db import models
from django.conf import settings

# Create your models here.


class BaseClass(models.Model):
    """ Abstract base model """
    create_ts = models.DateTimeField(auto_now=False, auto_now_add=True)
    modify_ts = models.DateTimeField(auto_now=True, auto_now_add=False)
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  default=1,
                                  on_delete=models.SET(1),
                                  related_name="%(app_label)s_%(class)s_create_by",
                                  null=False
                                  )
    modify_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  default=1,
                                  on_delete=models.SET(1),
                                  related_name="%(app_label)s_%(class)s_modify_by"
                                  )


class Quiz(BaseClass):
    """ Represents the general structure of a quiz """

    quiz_name = models.CharField(
        max_length=120,
        help_text="Name that can be used to identify a quiz",
        null=False,
        blank=False,
        unique=True)
    maximum_score = models.IntegerField(help_text="Highest score possible",
                                        default=0,
                                        null=True,
                                        blank=True)
    overall_record_score = models.IntegerField(
        help_text="Highest score ever recorded at this quiz",
        default=0,
        null=True,
        blank=True)
    personal_record_score = models.IntegerField(
        help_text="Highest score that your team has scored at this quiz",
        default=0,
        null=True,
        blank=True)
    rounds = models.IntegerField(
        help_text="Number of standard rounds in the quiz",
        default=0,
        null=True,
        blank=True)

    def __str__(self):
        return self.quiz_name

    class Meta:
        verbose_name_plural = "quizzes"


class QuizInstance(BaseClass):
    """ Represents one occurrence of a particular quiz """

    quiz_type = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    quiz_date = models.DateField(null=False, blank=False)
    team_size = models.IntegerField(null=False, blank=False)
    pints_consumed = models.IntegerField(null=True, blank=True)
    number_of_teams = models.IntegerField(
        help_text="Number of teams competing",
        null=True,
        blank=True)
    winning_score = models.IntegerField(
        help_text="Top score achieved by any one team",
        null=True,
        blank=True)
    teams_above_ninety = models.IntegerField(
        help_text="Number of teams that scored above 90 points",
        null=True,
        blank=True)
    bonus_score = models.IntegerField(
        help_text="Number of points scored on the bonus question",
        null=True,
        blank=True)

    class Meta:
        unique_together = ('quiz_date', 'quiz_type')

    def __str__(self):
        return self.quiz_type.quiz_name + " (" + self.quiz_date.strftime('%d-%m-%Y') + ")"


class RoundCategory(BaseClass):
    """ Represents the category of a particular QuizRound """

    category = models.CharField(max_length=120,
                                null=False,
                                blank=False,
                                unique=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "round categories"


class QuizRound(BaseClass):
    """ Represents a single round in the quiz """

    quiz_instance = models.ForeignKey(QuizInstance, on_delete=models.CASCADE)
    round_number = models.IntegerField(null=False, blank=False)
    category = models.ForeignKey(
        RoundCategory,
        null=False,
        blank=False,
        on_delete=models.PROTECT)
    score = models.IntegerField(null=False, blank=False)
    doubler = models.BooleanField(default=False)

    class Meta:
        unique_together = ('quiz_instance', 'round_number')

    def __str__(self):
        return self.quiz_instance.quiz_type.quiz_name + " (" + self.quiz_instance.quiz_date.strftime('%d-%m-%Y') + ") - " + self.category.category
