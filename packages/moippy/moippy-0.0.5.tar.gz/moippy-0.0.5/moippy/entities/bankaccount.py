# -*- coding: utf-8 -*-
from .lib import *

class BankAccount(MoipEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/bankaccounts'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id  = String(max=255)
		cls.type =  String(max=255)
		cls.status =  String(max=255)
		cls.bankNumber = String(max=255)
		cls.bankName =  String(max=255)
		cls.agencyNumber = Int()
		cls.agencyCheckNumber = String(max=10)
		cls.accountNumber = Int()
		cls.accountCheckNumber = String(max=10)
		cls.holder =  Obj(context=cls, key='holder', name='Holder')
		cls.createdAt =  String(max=255)
		cls._links = Dict()

		super().__init__(**kw)

	def Create(self, account_id: str):
		data = Post(f'/accounts/{account_id}/bankaccounts', self.toJSON(), None if self.resourceToken is None else {'resourceToken': self.resourceToken})
		self.load(**data)
		return self
