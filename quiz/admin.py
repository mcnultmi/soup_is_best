from django.contrib import admin
from .models import Quiz, QuizInstance, RoundCategory, QuizRound

# Register your models here.


class QuizAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':
                ['quiz_name']}),
        ('Scoring Information', {'fields': [
         'rounds', 'maximum_score', 'personal_record_score', 'overall_record_score']})
    ]

    list_display = (
        'quiz_name',
        'rounds',
        'maximum_score',
        'overall_record_score',
        'personal_record_score',
        'create_ts',
        'create_by',
        'modify_ts',
        'modify_by'
    )

    search_fields = ['quiz_name']


class QuizInstanceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':
                ['quiz_type', 'quiz_date']}),
        ('Additional Information', {'fields': [
         'team_size', 'winning_score', 'number_of_teams', 'teams_above_ninety', 'bonus_score', 'pints_consumed']})
    ]

    list_display = (
        'quiz_type',
        'quiz_date',
        'team_size',
        'winning_score',
        'create_ts',
        'create_by',
        'modify_ts',
        'modify_by'
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
        'quiz_instance',
        'round_number',
        'category',
        'score',
        'doubler',
        'create_ts',
        'create_by',
        'modify_ts',
        'modify_by'
    )

    search_fields = ['category']


admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizInstance, QuizInstanceAdmin)
admin.site.register(RoundCategory, RoundCategoryAdmin)
admin.site.register(QuizRound, QuizRoundAdmin)
