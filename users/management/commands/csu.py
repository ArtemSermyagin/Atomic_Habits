from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='root@mail.ru',
            telegram_chat_id=987134832,
            password='1234',
            is_superuser=True,
            is_staff=True,
        )
        user.set_password('1234')
        user.save()
