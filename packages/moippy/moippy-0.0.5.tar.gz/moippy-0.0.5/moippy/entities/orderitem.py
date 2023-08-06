# -*- coding: utf-8 -*-
from .lib import *

class OrderItem(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.product = String(max=255)
		cls.price = Int()
		cls.detail = String(max=255)
		cls.quantity = Int()
		cls.category = String()

		super().__init__(**kw)
