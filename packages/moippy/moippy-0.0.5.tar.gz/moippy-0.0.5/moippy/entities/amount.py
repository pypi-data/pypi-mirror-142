# -*- coding: utf-8 -*-
from .lib import *

class Amount(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.paid = Int()
		cls.fixed = Int()
		cls.amountValid = Int()
		cls.total = Int()
		cls.gross = Int()
		cls.addition = Int()
		cls.fees = Int()
		cls.deduction = Int()
		cls.refunds = Int()
		cls.liquid = Int()
		cls.otherReceivers = Int()
		cls.currency = String(max=3)
		cls.subtotals = Obj(context=cls, key='subtotals', name='Subtotal')

		super().__init__(**kw)
