
from moippy.utils.moip import *
from moippy import CreditCard


def AddCreditCard(customer_id: str, creditCard:CreditCard):
    data = Post(f"/customers/{customer_id}/fundinginstruments", {
        "method": "CREDIT_CARD",
        "creditCard": creditCard.toJSON(),
    })
    if 'creditCard' in data:
        creditCard.load(**data['creditCard'])

def DeleteCreditCard(creditcard_id: str):
    Delete(f"/fundinginstruments/{creditcard_id}", {})
