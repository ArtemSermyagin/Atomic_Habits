from rest_framework.serializers import ValidationError


def validate_related_or_reward(habit):
    if habit.related_habits and habit.reward:
        raise ValidationError('Необходимо выбрать либо вознаграждение, либо приятную привычку')


def validate_linked_habit(habit):
    if habit.related_habits and habit.sign_good_habit:
        raise ValidationError('В связанные привычки могут попадать только привычки с приятным признаком.')


def validate_reward_for_useful_habit(habit):
    if habit.sign_good_habit and (habit.related_habits or habit.reward):
        raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')
