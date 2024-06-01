from datetime import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import TelegramClient


@shared_task
def task_send_message():
    print(Habit.objects.filter(sign_good_habit=False))
    for habit in Habit.objects.filter(sign_good_habit=False):
        print(1, habit.time.strftime('%H:%M'), 2, datetime.now().time().strftime('%H:%M'))
        if (
                habit.time.strftime('%H:%M') == datetime.now().time().strftime('%H:%M')
                and
                habit.periodicity
        ):
            text_message = (
                f"Пора выполнить {habit.action}"
                f"У тебя есть примерно {habit.time_to_complete} секунд."
            )
            if habit.reward:
                text_message += f"\nА в виде вознаграждения получишь {habit.reward}."
            print(3, habit.user.telegram_chat_id)
            print(4, text_message)
            TelegramClient().send_message(
                text=text_message,
                chat_id=habit.user.telegram_chat_id
            )
            return "Success"
