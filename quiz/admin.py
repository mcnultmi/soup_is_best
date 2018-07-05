from django.contrib import admin
from .models import QuizBase, QuizInstance, RoundCategory, QuizRound

# Register your models here.


class QuizRoundInline(admin.TabularInline):
    model = QuizRound
    fk_name = 'quiz_instance'
    max_num = 8
    extra = 8
    fields = ['round_number', 'category', 'score', 'doubler']


class QuizBaseAdmin(admin.ModelAdmin):
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
                ['quiz', 'quiz_date']}),
        ('Additional Information', {'fields': [
         ('team_size', 'number_of_teams', 'teams_above_ninety'),
         ('winning_score', 'bonus_score')
         ]})
    ]

    inlines = [
        QuizRoundInline
    ]

    list_display = (
        'quiz',
        'quiz_date',
        'team_size',
        'winning_score',
        'create_ts',
        'create_by',
        'modify_ts',
        'modify_by'
    )

    list_filter = ['quiz_date']
    search_fields = ['quiz', 'quiz_date']


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


admin.site.register(QuizBase, QuizBaseAdmin)
admin.site.register(QuizInstance, QuizInstanceAdmin)
admin.site.register(RoundCategory, RoundCategoryAdmin)
admin.site.register(QuizRound, QuizRoundAdmin)
