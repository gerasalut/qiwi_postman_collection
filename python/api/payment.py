import pytest
import requests
import data.payments

class CreatingPayment():

    def __init__(self):
        self.payout_url = "https://api-test.qiwi.com/partner/payout/"

    def create_payment_spb(self, agent_id: str, point_id: str, payment_id:str):
        path_url = f"{self.payout_url}/v1/agents/{agent_id}/points/{point_id}/payments/{payment_id}"
        header = {
            'Authorization': self.auth_token()
        }
        response = requests.put(path_url, headers=header, json=data.payments.VALID_PAY_SBP)

    def create_payment_bank(self, agent_id: str, point_id: str, payment_id:str):
        path_url = f"{self.payout_url}/v1/agents/{agent_id}/points/{point_id}/payments/{payment_id}"
        header = {
            'Authorization': self.auth_token()
        }
        response = requests.put(path_url, headers=header, json=data.payments.VALID_PAY_BANK)