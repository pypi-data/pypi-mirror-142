# -*- coding: utf-8 -*-
from .lib import *

class Transfer(MoipEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/transfers'
		cls.__metadata__ = {}
		cls.__requireid__ = True
		
		# FIELDS
		cls.id = String(max=155)
		cls.ownId = String(max=155)
		cls.fee = Int()
		cls.amount = Int()
		cls.description = String(max=255)
		cls.status = String(max=155)
		cls.role = String(max=50)
		cls.transferInstrument =  Obj(context=cls, key='transferInstrument', name='TransferInstrument')
		cls.events =  ObjList(context=cls, key='events', name='Event')
		cls.cancellationDetails = Obj(context=cls, key='cancellationDetails', name='CancellationDetails')
		cls.entries =  ObjList(context=cls, key='entries', name='Entrie')
		cls.createdAt = String(max=155)
		cls.updatedAt = String(max=155)
		cls._links = Dict()

		super().__init__(**kw)

	def Reverse(self, transfer_id:str):
		data = Post(f"transfers/{transfer_id}/reverse", {})
		self.load(**data)
		return self
