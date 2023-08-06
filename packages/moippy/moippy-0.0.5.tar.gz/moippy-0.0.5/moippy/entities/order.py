# -*- coding: utf-8 -*-
from .lib import *

class Order(MoipEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/orders'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=65)
		cls.ownId = String(max=65)
		cls.status = String(max=65)
		cls.platform =  String(max=65)
		cls.createdAt = String(max=65)
		cls.updatedAt = String(max=65)
		cls.amount = Obj(context=cls, key='amount', name='Amount')
		cls.items = ObjList(context=cls, key='items', name='OrderItem')
		cls.checkoutPreferences = Obj(context=cls, key='checkoutPreferences', name='CheckoutPreference')
		cls.receivers = ObjList(context=cls, key='receivers', name='Receiver')
		cls.customer = Obj(context=cls, key='customer', name='Customer')
		cls.addresses = ObjList(context=cls, key='addresses', name='Address')
		cls.payments = ObjList(context=cls, key='payments', name='Payment')
		cls.escrows = ObjList(context=cls, key='escrows', name='Escrow')
		cls.refunds = ObjList(context=cls, key='refunds', name='Refund')
		cls.entries = ObjList(context=cls, key='entries', name='Entrie')
		cls.events = ObjList(context=cls, key='events', name='Event')
		cls._links = Dict()

		super().__init__(**kw)
