from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='artem@gmail.com',
            password='admin_password'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            user=self.user,
            place="Улица",
            time="10:00",
            action="Пробежка",
            time_to_complete=100,
            periodicity='every_day'
        )

    def test_habit_create(self):
        data = {
            "place": "Дом",
            "time": "21:00",
            "action": "Спать",
            "time_to_complete": "100",
            "periodicity": "every_day",
            "sign_good_habit": "True"
        }
        response = self.client.post(reverse('habits:habit_list_create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {
            'id': 2,
            'place': 'Дом',
            'time': '21:00:00',
            'action': 'Спать',
            'sign_good_habit': True,
            'periodicity': 'every_day',
            'reward': None,
            'time_to_complete': 100,
            'is_public': False,
            'user': None,
            'related_habits': None
        })

    def test_habit_list(self):
        response = self.client.get(reverse('habits:habit_list_create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_detail(self):
        response = self.client.get(
            reverse('habits:habits_retrieve_update_destroy', kwargs={'pk': self.habit.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_delete(self):
        """ Удаления Привычки """
        response = self.client.delete(
            reverse('habits:habits_retrieve_update_destroy', kwargs={'pk': self.habit.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.filter(id=self.habit.pk).count(), 0)

    def test_habit_update(self):
        data = {
            'place': 'Работа',
            'time': '18:00',
            'action': 'Уходить домой',
            'sign_good_habit': 'True'
        }
        response = self.client.patch(
            reverse(
                'habits:habits_retrieve_update_destroy',
                kwargs={'pk': self.habit.pk}
            ),
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reward_and_pleasant_habit(self):
        """Тестирование создания привычки с наградой и приятной привычкой одновременно"""
        data = {
            "place": "Дом",
            "time": "21:00",
            "action": "Играть в игры",
            "time_to_complete": "100",
            "periodicity": "every_day",
            "sign_good_habit": "True",
            "reward": "Общение с друзьями"
        }
        response = self.client.post(reverse('habits:habit_list_create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_reward_for_useful_habit(self):
        """Тестирование Только полезные привычки могут иметь награду"""
        data = {
            "place": "Дом",
            "time": "21:00",
            "action": "Спать",
            "time_to_complete": "100",
            "periodicity": "every_day",
            "sign_good_habit": "True",
            "reward": "Мороженное"
        }
        response = self.client.post(reverse('habits:habit_list_create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_related_or_reward(self):
        """Тестирование либо вознаграждение, либо приятная привычка """
        data = {
            "place": "Дом",
            "time": "21:00",
            "action": "Спать",
            "time_to_complete": "100",
            "periodicity": "every_day",
            "sign_good_habit": "True",
            "reward": "Мороженное"
        }
        response = self.client.post(reverse('habits:habit_list_create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
