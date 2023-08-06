# -*- coding: utf-8 -*-
from .lib import *

class OnlineBankDebit(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.bankNumber = String(max=55)
		cls.expirationDate = DateTime()
		cls.returnUri = String(max=255)

		super().__init__(**kw)
