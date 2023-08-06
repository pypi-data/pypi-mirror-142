
from moippy.utils.moip import *
from moippy import Statement, Entrie
from moippy.entities.lib.datatype import ListType

def Statements(begin:str, end:str):
    data = Get(f"/statements?begin={begin}&end={end}")
    return ListType(Statement).add([Statement(**item) for item in data["lines"]]) if "lines" in data  and isinstance(data["lines"], list) else ListType(Statement)

def DetailStatement(type:str, date:str):
    data = Get(f"/statements/details?type={type}&date={date}")
    return ListType(Entrie).add([Entrie(**item) for item in data["entries"]]) if "entries" in data  and isinstance(data["entries"], list) else ListType(Entrie)

def FutureStatements(begin:str, end:str):
    data = Get(f"/futurestatements?begin={begin}&end={end}")
    return ListType(Statement).add([Statement(**item) for item in data["lines"]]) if "lines" in data  and isinstance(data["lines"], list) else ListType(Statement)

def DetailFutureStatement(type:str, date:str):
    data = Get(f"/futurestatements/details?type={type}&date={date}")
    return ListType(Entrie).add([Entrie(**item) for item in data["entries"]]) if "entries" in data  and isinstance(data["entries"], list) else ListType(Entrie)

def Entries(entry_id=''):
    if entry_id != '':
        data = Get(f"/entries/{entry_id}")
        return Entrie(**data) if data else None
    else:
        data = Get(f"/entries")
        return ListType(Entrie).add([Entrie(**item) for item in data]) if isinstance(data, list) else ListType(Entrie)
