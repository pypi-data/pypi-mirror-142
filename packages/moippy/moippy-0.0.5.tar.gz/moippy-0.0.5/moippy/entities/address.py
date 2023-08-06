# -*- coding: utf-8 -*-
from .lib import *

class Address(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.street = String(max=255)
		cls.streetNumber = String(max=255)
		cls.complement = String(max=255)
		cls.district = String(max=255)
		cls.city = String(max=255)
		cls.state = String(max=255)
		cls.country = String(max=255)
		cls.zipCode = Int()
		cls.type = String(max=255)

		super().__init__(**kw)
