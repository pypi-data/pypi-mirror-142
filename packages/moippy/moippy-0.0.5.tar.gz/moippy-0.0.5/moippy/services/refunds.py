
from moippy.utils.moip import *
from moippy import Refund
from moippy.entities.lib.datatype import ListType

def Refunds(item_id:str):
    item_type = "payments" if item_id.startswith("PAY") else "orders"
    data = Get(f"/{item_type}/{item_id}/refunds")
    return ListType(Refund).add([Refund(**item) for item in data["refunds"]]) if "refunds" in data and isinstance(data["refunds"], list) else ListType(Refund)
