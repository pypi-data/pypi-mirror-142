# -*- coding: utf-8 -*-
from .lib import *

class CreditCard(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=65)
		cls.hash = String(max=1000)
		cls.number = String(max=65)
		cls.expirationMonth = String(max=2)
		cls.expirationYear = String(max=4)
		cls.cvc  = String(max=255)
		cls.brand = String(max=255)
		cls.first6 = String(max=6)
		cls.last4 = String(max=4)
		cls.holder = Obj(context=cls, key='holder', name='Holder')
		cls.store = Boolean()

		super().__init__(**kw)
