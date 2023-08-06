# -*- coding: utf-8 -*-
from .lib import *

class Event(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=55)
		cls.description = String(max=255)
		cls.createdAt = String(max=255)
		cls.type = String(max=255)


		super().__init__(**kw)
