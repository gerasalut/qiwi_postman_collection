import pytest
import requests

class AccessService():

    def __init__(self):
        self.BASE_URL = "https://api-test.qiwi.com/partner/accounts/"
        self.auth_token = ""

#Получаем привязанные карты/счета пользователя
    def get_account_card(self, user_id: int):
        header = {
            'Authorization': self.auth_token()
        }
        path_url = f"{self.BASE_URL}/{user_id}"
        response = requests.get(path_url, headers=header)
        return response.json(), response.status_code

