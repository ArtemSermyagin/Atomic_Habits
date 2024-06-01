from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from users.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='artem@gmail.com',
            telegram_chat_id=987134832,
            password='admin_password'
        )

    def test_user_create(self):
        data = {
            "email": "adminTest@mail.ru",
            "telegram_chat_id": 54321,
            "password": "admin_password"
        }
        response = self.client.post(reverse('users:users_create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_detail(self):
        response = self.client.get(
            reverse(
                'users:users_retrieve_update_destroy',
                kwargs={'pk': self.user.pk}
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete(self):
        response = self.client.delete(
            reverse(
                'users:users_retrieve_update_destroy',
                kwargs={'pk': self.user.pk}
            )
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.filter(id=self.user.pk).count(), 0)

    def test_user_update(self):
        update_url = reverse(
            'users:users_retrieve_update_destroy',
            kwargs={'pk': self.user.pk}
        )
        update_data = {'phone': '89997776655'}
        response = self.client.patch(update_url, update_data, format='json')
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user.phone, update_data['phone'])
