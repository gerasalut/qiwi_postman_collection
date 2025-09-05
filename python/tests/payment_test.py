import pytest

## Создание заявки платежа на СПБ
def test_creating_payment_spb(payment):
    response = payment.create_payment_spb("acme", "000100", "b100-00100-b200")
    data = response.json()
    assert response.status_code == 200
    assert "paymentId" in data, "Нет paymentId"
    assert "creationDateTime" in data, "Нет creationDateTime"
    assert "expirationDatetime" in data, "Нет expirationDatetime"
    assert "status" in data, "Нет status"
    assert "recipientDetails" in data, "Нет recipientDetails"
    assert "amount" in data, "Нет amount"

## Создание заявки платежа на банковскую карту
def test_creating_payment_bank(payment):
    response = payment.create_payment_bank("acme", "000200", "b200-00200-b300")
    assert response.status_code == 200