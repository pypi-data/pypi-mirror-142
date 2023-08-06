# -*- coding: utf-8 -*-
from .lib import *

class Phone(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.countryCode = String(max=2)
		cls.areaCode = String(max=2)
		cls.number = String(max=16)
		cls.verified = Boolean()
		cls.phoneType = String(max=20)

		super().__init__(**kw)
