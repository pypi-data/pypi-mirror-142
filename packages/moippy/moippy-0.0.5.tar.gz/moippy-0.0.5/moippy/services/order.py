
from moippy.utils.moip import *
from moippy import Order
from moippy.entities.lib.datatype import ListType

def Orders():
    data = Get(f"/orders")
    return ListType(Order).add([Order(**item) for item in data["orders"]]) if "orders" in data and isinstance(data["orders"], list) else ListType(Order)
