# -*- coding: utf-8 -*-
from .lib import *

class TransferInstrument(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.method = String(max=155)
		cls.bankAccount = Obj(context=cls, key='bankAccount', name='BankAccount')
		cls.moipAccount = Obj(context=cls, key='moipAccount', name='MoipAccount')

		super().__init__(**kw)
