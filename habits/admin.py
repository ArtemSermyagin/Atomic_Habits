from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'place',
        'time',
        'action',
        'sign_good_habit',
        'related_habits',
        'periodicity',
        'reward',
        'time_to_complete',
        'is_public'
    )
    search_fields = ('sign_good_habit', 'is_public',)
