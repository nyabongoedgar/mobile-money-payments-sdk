import os

class MomoConfig:
    @staticmethod
    def get_config():
        return {
            'username': os.getenv('MOMO_USERNAME'),
            'password': os.getenv('MOMO_PASSWORD'),
            'subscription_id': os.getenv('MOMO_SUBSCRIPTION_ID'),
            'callback_url': os.getenv('MOMO_CALLBACK_URL')
        }
