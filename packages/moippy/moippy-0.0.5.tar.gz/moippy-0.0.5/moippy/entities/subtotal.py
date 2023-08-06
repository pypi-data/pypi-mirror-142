# -*- coding: utf-8 -*-
from .lib import *

class Subtotal(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.shipping = Int()
		cls.addition = Int()
		cls.discount = Int()
		cls.items = Int()


		super().__init__(**kw)
