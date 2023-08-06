# -*- coding: utf-8 -*-
from .lib import *

class App(MoipEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/channels'
		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=255)
		cls.name = String(max=255)
		cls.accessToken = String(max=255)
		cls.description = String(max=255)
		cls.website = String(max=255)
		cls.site = String(max=255)
		cls.secret = String(max=255)
		cls.redirectUri = String(max=255)
		cls.createdAt =String(max=255)
		cls.updatedAt = String(max=255)

		super().__init__(**kw)
