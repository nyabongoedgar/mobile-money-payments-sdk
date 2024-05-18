import requests
import base64
import uuid

class MomoApiClient:
    def __init__(self, username, password, subscription_id, callback_url):
        self.username = username
        self.password = password
        self.subscription_id = subscription_id
        self.callback_url = callback_url
        self.headers = {
            'Authorization': 'Basic ' + base64.b64encode(f"{username}:{password}".encode()).decode(),
            'Ocp-Apim-Subscription-Key': subscription_id,
            'X-Callback-Url': callback_url,
            'X-Reference-Id': str(uuid.uuid4())
        }

    def initiate_payment(self, amount, currency, payer_phone):
        payload = {
            "amount": amount,
            "currency": currency,
            "externalId": str(uuid.uuid4()),
            "payer": {
                "partyIdType": "MSISDN",
                "partyId": payer_phone
            },
            "payerMessage": "Test payment",
            "payeeNote": "Thank you for your payment."
        }
        response = requests.post("https://api.momodeveloper.mtn.com/collection/v1_0/", headers=self.headers, json=payload)
        return response.json()
