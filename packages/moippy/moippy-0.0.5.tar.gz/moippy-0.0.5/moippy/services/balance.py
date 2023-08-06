
from moippy.utils.moip import *
from moippy import BankAccount
from moippy.entities.lib.datatype import ListType

def Balance(resourceToken=None):
    data = Get(f"/balances", aditional_header={'resourceToken':resourceToken} if resourceToken else None)
    for item in data:
        del item['_links']
    return data[0]
