# -*- coding: utf-8 -*-
from .lib import *

class MoipAccount(MoipEntity):

	def __init__(cls, **kw):
		cls.__route__ = "/accounts"
		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=65)
		cls.login = String(max=65)
		cls.fullname = String(max=65)
		cls.accessToken = String(max=255)
		cls.channelId = String(max=255)
		cls.type = String(max=65)
		cls.transparentAccount = Boolean()
		cls.email = Obj(context=cls, key='email', name='Email')
		cls.person = Obj(context=cls, key='person', name='Person')
		super().__init__(**kw)
