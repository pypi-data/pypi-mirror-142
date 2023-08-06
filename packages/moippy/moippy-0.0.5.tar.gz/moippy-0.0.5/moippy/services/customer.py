
from moippy.utils.moip import *
from moippy import Customer
from moippy.entities.lib.datatype import ListType

def Customers():
    data = Get(f"/customers")
    return ListType(Customer).add([Customer(**item) for item in data]) if isinstance(data, list) else ListType(Customer)
