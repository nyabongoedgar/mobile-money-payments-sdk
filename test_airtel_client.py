import unittest
from unittest.mock import patch
import requests
from airtel_client import AirtelMoneyPaymentClient # Make sure to replace 'your_module' with the actual module name

class TestAirtelMoneyPaymentClient(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://openapiuat.airtel.africa/"
        self.client_id = "test_client_id"
        self.client_secret = "test_client_secret"
        self.airtel_client = AirtelMoneyPaymentClient(self.base_url, self.client_id, self.client_secret)

    @patch('requests.post')
    def test_fetch_access_token_success(self, mock_post):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "access_token": "test_access_token"
        }
        mock_post.return_value = mock_response

        access_token = self.airtel_client.fetch_access_token()
        self.assertEqual(access_token, "test_access_token")
        self.assertEqual(self.airtel_client.access_token, "test_access_token")

    @patch('requests.post')
    def test_fetch_access_token_failure(self, mock_post):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        with self.assertRaises(Exception) as context:
            self.airtel_client.fetch_access_token()

        self.assertTrue('Failed to fetch access token' in str(context.exception))

    @patch('requests.post')
    def test_initiate_payment_success(self, mock_post):
        # First mock the access token retrieval
        mock_response_token = unittest.mock.Mock()
        mock_response_token.status_code = 200
        mock_response_token.json.return_value = {
            "access_token": "test_access_token"
        }
        mock_post.side_effect = [mock_response_token]

        self.airtel_client.fetch_access_token()

        # Now mock the payment initiation
        mock_response_payment = unittest.mock.Mock()
        mock_response_payment.status_code = 200
        mock_response_payment.json.return_value = {
            "status": "success",
            "transaction_id": "unique_transaction_id"
        }
        mock_post.side_effect = [mock_response_token, mock_response_payment]

        payment_response = self.airtel_client.initiate_payment(
            reference="12345",
            subscriber_msisdn="+256712345678",
            transaction_amount=1000,
            transaction_country="UG",
            transaction_currency="UGX",
            transaction_id="unique_transaction_id"
        )
        print(f'{payment_response} response is here')
        self.assertEqual(payment_response['transaction_id'], "unique_transaction_id")

    @patch('requests.post')
    def test_initiate_payment_failure(self, mock_post):
        # First mock the access token retrieval
        mock_response_token = unittest.mock.Mock()
        mock_response_token.status_code = 200
        mock_response_token.json.return_value = {
            "access_token": "test_access_token"
        }
        mock_post.side_effect = [mock_response_token]

        self.airtel_client.fetch_access_token()

        # Now mock the payment initiation
        mock_response_payment = unittest.mock.Mock()
        mock_response_payment.status_code = 400
        mock_response_payment.json.return_value = {
            "status": "failure",
            "error": "Invalid request"
        }
        mock_post.side_effect = [mock_response_token, mock_response_payment]

        payment_response = self.airtel_client.initiate_payment(
            reference="12345",
            subscriber_msisdn="+256712345678",
            transaction_amount=1000,
            transaction_country="UG",
            transaction_currency="UGX",
            transaction_id="unique_transaction_id"
        )

        self.assertEqual(payment_response['status'], "failure")
        self.assertEqual(payment_response['error'], "Invalid request")

if __name__ == '__main__':
    unittest.main()
