from rest_framework import serializers

from habits.models import Habit
from habits.validators import (
    validate_linked_habit,
    validate_reward_for_useful_habit,
    validate_related_or_reward
)


class HabitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
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

    def validate(self, data):
        habit = Habit(**data)
        validate_linked_habit(habit)
        validate_reward_for_useful_habit(habit)
        validate_related_or_reward(habit)
        return data
