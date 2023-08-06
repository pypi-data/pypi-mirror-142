# -*- coding: utf-8 -*-
from .lib import *
from .fundinginstrument import FundingInstrument

class WebhookPreference(MoipEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/preferences/notifications'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=55)
		cls.events = ObjList(context=cls, key='events', name='str')
		cls.target = String(max=655)
		cls.media = String(max=255)
		cls.token = String(max=55)

		super().__init__(**kw)
