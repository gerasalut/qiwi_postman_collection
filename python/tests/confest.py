import pytest
from api.access import AccessService
from api.balance import Balance
from api.executie import ExecutePayment
from api.payment import CreatingPayment


@pytest.fixture()
def access_service():
    return AccessService()

@pytest.fixture()
def balance():
    return Balance()

@pytest.fixture()
def execute():
    return ExecutePayment()

@pytest.fixture()
def payment():
    return CreatingPayment()