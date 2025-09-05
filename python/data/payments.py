VALID_PAY_SBP = {
            "recipientDetails": {
                "providerCode": "sbp-b2c",
                "fields": {
                    "account": "79098087755",
                    "bankId": "100000000001"
                }
            },
            "amount": {
                "value": "1.00",
                "currency": "RUB"
            },
            "source": {
                "paymentType": "NO_EXTRA_CHARGE",
                "paymentToolType": "BANK_ACCOUNT",
                "paymentTerminalType": "MOBILE_BANKING"
              }
}

VALID_PAY_BANK = {
             "recipientDetails": {
                "providerCode": "bank-card-russia",
                "fields": {
                   "pan": "123456******4321"
                }
              },
              "amount": {
                "value": "1.00",
                "currency": "RUB"
              },
              "source": {
                "paymentType": "NO_EXTRA_CHARGE",
                "paymentToolType": "BANK_ACCOUNT",
                "paymentTerminalType": "INTERNET_BANKING"
              }
            }


