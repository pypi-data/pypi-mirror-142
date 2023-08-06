# -*- coding: utf-8 -*-
from .lib import *
from .fundinginstrument import FundingInstrument

class Refund(MoipEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/refunds'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=55)
		cls.status = String(max=55)
		cls.events = ObjList(context=cls, key='events', name='Event')
		cls.amount = Obj(context=cls, key='amount', name='Amount')
		cls.type = String(max=55)
		cls.refundingInstrument = Obj(context=cls, key='refundingInstrument', name='FundingInstrument')
		cls.createdAt = String(max=55)
		cls._links = Dict()

		super().__init__(**kw)

	def Create(self, item_id: str, amount:int, refundingInstrument:FundingInstrument or None = None):
		item_type = "payments" if item_id.startswith("PAY") else "orders"
		data = Post(f'/{item_type}/{item_id}/refunds', {'amount': amount, 'refundingInstrument' : refundingInstrument.toJSON() if refundingInstrument else None})
		self.load(**data)
		return self
