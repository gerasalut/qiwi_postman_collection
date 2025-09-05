import pytest
import requests

class ExecutePayment():

    def __init__(self):
        self.payout_url = "https://api-test.qiwi.com/partner/payout/"

    def execute_payment(self, agent_id:str, point_id:str, payment_id:str):
        path_url = f"{self.payout_url}v1/agents/{agent_id}/points/{point_id}/payments/{payment_id}/execute"
        header = {
            'Authorization': self.auth_token()
        }
        requests.post(path_url, headers=header)