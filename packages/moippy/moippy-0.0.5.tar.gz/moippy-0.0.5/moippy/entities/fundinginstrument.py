# -*- coding: utf-8 -*-
from .lib import *

class FundingInstrument(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.method = String(max=65)
		cls.creditCard = Obj(context=cls, key='creditCard', name='CreditCard')
		cls.boleto = Obj(context=cls, key='boleto', name='Boleto')
		cls.onlineBankDebit = Obj(context=cls, key='onlineBankDebit', name='OnlineBankDebit')

		super().__init__(**kw)
