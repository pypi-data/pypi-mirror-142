# -*- coding: utf-8 -*-
from .lib import *


class Payment(MoipEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/payments'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=55)
		cls.installmentCount = Int()
		cls.amount = Obj(context=cls, key='amount', name='Amount')
		cls.cancellationDetails = Obj(context=cls, key='cancellationDetails', name='CancellationDetails')
		cls.fundingInstrument = Obj(context=cls, key='fundingInstrument', name='FundingInstrument')
		cls.delayCapture = Boolean()
		cls.statementDescriptor = String(max=13)
		cls.escrow = Obj(context=cls, key='escrow', name='Escrow')
		cls.device = Obj(context=cls, key='device', name='Device')
		cls.fingerprint = String(max=255)
		cls.status = String(max=55)
		cls.fees = ObjList(context=cls, key='fees', name='Fee')
		cls.events = ObjList(context=cls, key='events', name='Event')
		cls.receivers = ObjList(context=cls, key='receivers', name='Receiver')
		cls._links = Dict()
		cls.createdAt = String(max=255)
		cls.updatedAt = String(max=255)
		super().__init__(**kw)

	def Capture(self):
		data = Post(f'{self.__route__}/{self.id}/capture', self.toJSON())
		self.load(**data)
		return self

	def Cancel(self):
		data = Post(f'{self.__route__}/{self.id}/void', self.toJSON())
		self.load(**data)
		return self

	def Create(self, order_id: str):
		data = Post(f'/orders/{order_id}/payments', self.toJSON())
		self.load(**data)
		return self
