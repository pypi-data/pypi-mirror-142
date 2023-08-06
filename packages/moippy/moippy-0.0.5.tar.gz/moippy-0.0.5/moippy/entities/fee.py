# -*- coding: utf-8 -*-
from .lib import *

class Fee(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.type = String(max=55)
		cls.amount = Int()


		super().__init__(**kw)
