from django.contrib import admin
from .models import Quiz, QuizInstance, RoundCategory, QuizRound

# Register your models here.


class QuizAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':
                ['quiz_name']}),
        ('Scoring Information', {'fields': [
         'number_of_rounds', 'personal_record_score', 'overall_record_score']})
    ]

    list_display = (
        'quiz_name', 'number_of_rounds', 'overall_record_score', 'personal_record_score'
    )

    search_fields = ['quiz_name']


class QuizInstanceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':
                ['quiz_name', 'quiz_date']}),
        ('Additional Information', {'fields': [
         'team_size', 'top_score', 'number_of_teams', 'teams_above_ninety', 'bonus_score', 'pints_consumed']})
    ]

    list_display = (
        'quiz_name', 'quiz_date', 'team_size', 'top_score'
    )

    list_filter = ['quiz_date']
    search_fields = ['quiz_name', 'quiz_date']


class RoundCategoryAdmin(admin.ModelAdmin):
    fields = ['category']
    search_fields = ['category']


class QuizRoundAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':
                ['quiz_instance']}),
        ('Round Information', {'fields': [
         'round_number', 'category', 'score', 'doubler']})
    ]

    list_display = (
        'quiz_instance', 'round_number', 'category', 'score', 'doubler'
    )

    search_fields = ['category']


admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizInstance, QuizInstanceAdmin)
admin.site.register(RoundCategory, RoundCategoryAdmin)
admin.site.register(QuizRound, QuizRoundAdmin)
