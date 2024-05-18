import requests
import json

class AirtelMoneyPaymentClient:
    STAGING_BASE_URL = "https://openapiuat.airtel.africa/"
    PRODUCTION_BASE_URL = "https://openapi.airtel.africa/"

    def __init__(self, base_url, client_id, client_secret):
        self.base_url = base_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None

    def fetch_access_token(self):
        auth_url = f"{self.base_url}/auth/oauth2/token"
        headers = {
            "Content-Type": "application/json",
            "Accept": "*/*"
        }
        body = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }
        response = requests.post(auth_url, headers=headers, data=json.dumps(body))
        if response.status_code == 200:
            data = response.json()
            self.access_token = data.get("access_token")
            return self.access_token
        else:
            raise Exception("Failed to fetch access token")

    def initiate_payment(self, reference, subscriber_msisdn, transaction_amount, transaction_country=None, transaction_currency=None, transaction_id=None):
        if not self.access_token:
            self.fetch_access_token()

        url = f"{self.base_url}merchant/v2/payments/"
        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'X-Country': transaction_country,
            'X-Currency': transaction_currency,
            'Authorization': f'Bearer {self.access_token}',
            'x-signature': '',  # Placeholder, actual value should be generated
            'x-key': ''  # Placeholder, actual value should be generated
        }
        body = {
            "reference": reference,
            "subscriber": {
                "country": transaction_country,
                "msisdn": subscriber_msisdn
            },
            "transaction": {
                "amount": transaction_amount,
                "id": transaction_id
            }
        }
        response = requests.post(url, headers=headers, data=json.dumps(body))
        return response.json()


"""
if __name__ == "__main__":
    # Replace these with your actual credentials and values
    base_url = "https://openapiuat.airtel.africa/"  # Use staging or production URL as needed
    client_id = "your_client_id"
    client_secret = "your_client_secret"
    
    airtel_client = AirtelMoneyPaymentClient(base_url, client_id, client_secret)
    
    # Fetch access token
    access_token = airtel_client.fetch_access_token()
    print(f"Fetched Access Token: {access_token}")

    # Example payment initiation
    payment_response = airtel_client.initiate_payment(
        reference="12345",  # Reference for service/goods purchased
        subscriber_msisdn="+256712345678",  # MSISDN without country code
        transaction_amount=1000,  # Amount in smallest currency unit (e.g., cents for USD)
        transaction_country="UG",  # Country code
        transaction_currency="UGX",  # Currency code
        transaction_id="unique_transaction_id"  # Partner unique transaction ID
    )
    print(payment_response)


"""