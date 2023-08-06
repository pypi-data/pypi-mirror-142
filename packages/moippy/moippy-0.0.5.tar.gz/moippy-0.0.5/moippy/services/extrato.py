
from moippy.utils.moip import *
from moippy import Webhook, WebhookPreference
from moippy.entities.lib.datatype import ListType

def WebhooksPreferences():
    data = Get(f"/preferences/notifications")
    return ListType(WebhookPreference).add([WebhookPreference(**item) for item in data]) if isinstance(data, list) else ListType(WebhookPreference)


def Webhooks(resourceId:str=None):
    data = Get(f"/webhooks?resourceId={resourceId}" if resourceId else "/webhooks")
    return ListType(Webhook).add([Webhook(**item) for item in data["webhooks"]]) if "webhooks" in data and isinstance(data["webhooks"], list) else ListType(Webhook)
