import pytest
import requests

class Balance():

    def __init__(self):
        self.payout_url = "https://api-test.qiwi.com/partner/payout/"

    def get_balance(self, agent_id: str, point_id: str):
        url = f"{self.payout_url}/v1/agents/{agent_id}/points/{point_id}/balance"
        header = {
            'Authorization': self.auth_token()
        }
        response = requests.get(url, headers=header)
        return response
