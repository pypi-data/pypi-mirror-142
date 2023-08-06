# -*- coding: utf-8 -*-
from .lib import *

class CheckoutPreference(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.redirectUrls = Obj(context=cls, key='redirectUrls', name='RedirectUrl')
		cls.installments = Obj(context=cls, key='installments', name='Installment')


		super().__init__(**kw)
