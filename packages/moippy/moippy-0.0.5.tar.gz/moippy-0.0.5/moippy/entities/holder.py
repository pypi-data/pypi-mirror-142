# -*- coding: utf-8 -*-
from .lib import *

class Holder(MoipEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/customers'
		cls.__metadata__ = {}

		# FIELDS
		cls.fullname = String(max=90)
		cls.birthDate = DateTime(format="%Y-%m-%d")
		cls.taxDocument = Obj(context=cls, key='taxDocument', name='TaxDocument')
		cls.phone = Obj(context=cls, key='phone', name='Phone')
		cls.billingAddress = Obj(context=cls, key='billingAddress', name='Address')

		super().__init__(**kw)
