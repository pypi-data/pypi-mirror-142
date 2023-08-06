# -*- coding: utf-8 -*-
from .lib import *

class Customer(MoipEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/customers'
		cls.__metadata__ = {}
		cls.__requireid__ = True
		
		# FIELDS
		cls.id = String(max=65)
		cls.ownId = String(max=65)
		cls.fullname = String(max=90)
		cls.email = String(max=90)
		cls.birthDate = DateTime(format="%Y-%m-%d")
		cls.createdAt = String(max=90)
		cls.taxDocument = Obj(context=cls, key='taxDocument', name='TaxDocument')
		cls.phone = Obj(context=cls, key='phone', name='Phone')
		cls.shippingAddress = Obj(context=cls, key='shippingAddress', name='Address')
		cls.addresses = ObjList(context=cls, key='addresses', name='Address')
		cls.fundingInstrument = Obj(context=cls, key='fundingInstrument', name='FundingInstrument')
		cls._links = Dict()

		super().__init__(**kw)
