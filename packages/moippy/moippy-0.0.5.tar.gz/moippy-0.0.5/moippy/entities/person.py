# -*- coding: utf-8 -*-
from .lib import *

class Person(MoipEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/customers'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.name = String(max=155)
		cls.lastName =String(max=155)
		cls.birthDate = DateTime(format="%Y-%m-%d")
		cls.taxDocument = Obj(context=cls, key='taxDocument', name='TaxDocument')
		cls.address = Obj(context=cls, key='address', name='Address')
		cls.phone = Obj(context=cls, key='phone', name='Phone')
		cls.identityDocument = Obj(context=cls, key='identitydocument', name='IdentityDocument')

		super().__init__(**kw)
