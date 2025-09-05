import pytest

## Тест на получение привязанной карты/счета
def test_get_account_card(access_service):
    response = access_service.get_account_card(500400333)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list), "Ответ должен быть массивом"
    assert len(data) > 0, "Если список счетов пустой"

    for account in data:
        # Проверки наличия ключевых полей
        assert "accountId" in account, "Нет accountId"
        assert "maskedPan" in account, "Нет maskedPan"
        assert "status" in account, "Нет status"
        assert "balance" in account, "Нет balance"

## Тест на получение привязаннной карты/счета с некорректным userId
def test_get_invalid_account_card(access_service):
    response = access_service().get_account_card(000000000)
    assert response.status_code == 404