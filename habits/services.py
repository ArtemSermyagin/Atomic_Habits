import os
import requests


class TelegramClient:
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    url = f'https://api.telegram.org/bot{token}/sendMessage'

    def send_message(self, text, chat_id):
        requests.post(
            url=f'{self.url}{self.token}/sendMessage',
            data={
                'chat_id': chat_id,
                'text': text
            }
        )
