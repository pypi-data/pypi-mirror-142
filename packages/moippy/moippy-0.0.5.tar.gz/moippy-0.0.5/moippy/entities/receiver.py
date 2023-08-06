# -*- coding: utf-8 -*-
from .lib import *

class Receiver(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.type = String(max=255)
		cls.feePayor = Boolean()
		cls.moipAccount = Obj(context=cls, key='moipAccount', name='MoipAccount')
		cls.amount = Obj(context=cls, key='amount', name='Amount')


		super().__init__(**kw)
