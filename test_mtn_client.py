import unittest
from unittest.mock import patch
import requests
from mtn_client import MomoApiClient  # Adjust this import based on the actual module name

class TestMomoApiClient(unittest.TestCase):

    def setUp(self):
        self.username = "test_username"
        self.password = "test_password"
        self.subscription_id = "test_subscription_id"
        self.callback_url = "https://example.com/callback"
        self.momo_client = MomoApiClient(self.username, self.password, self.subscription_id, self.callback_url)

    @patch('requests.post')
    def test_initiate_payment_success(self, mock_post):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "success",
            "message": "Payment initiated successfully"
        }
        mock_post.return_value = mock_response

        response = self.momo_client.initiate_payment(
            amount="1000",
            currency="USD",
            payer_phone="+1234567890"
        )

        self.assertEqual(response['message'], "Payment initiated successfully")

    @patch('requests.post')
    def test_initiate_payment_failure(self, mock_post):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 400
        mock_response.json.return_value = {
            "status": "failure",
            "error": "Invalid request"
        }
        mock_post.return_value = mock_response

        response = self.momo_client.initiate_payment(
            amount="1000",
            currency="USD",
            payer_phone="+1234567890"
        )

        self.assertEqual(response['error'], "Invalid request")

if __name__ == '__main__':
    unittest.main()
