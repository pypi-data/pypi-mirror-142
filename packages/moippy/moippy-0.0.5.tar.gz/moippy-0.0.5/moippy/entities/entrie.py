# -*- coding: utf-8 -*-
from .lib import *

class Entrie(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=55)
		cls.ownId = String(max=55)
		cls.external_id = String(max=55)
		cls.reschedule = Obj(context=cls, key='reschedule', name='str')
		cls.scheduledFor = String(max=155)
		cls.status = String(max=155)
		cls.type = String(max=155)
		cls.updatedAt = String(max=155)
		cls.amount = Obj(context=cls, key='amount', name='Amount')
		cls.moipAccount = Obj(context=cls, key='moipAccount', name='MoipAccount')
		cls.fees = Obj(context=cls, key='fees', name='Fee')
		cls.operation = String(max=155)
		cls.createdAt = String(max=155)
		cls.event = String(max=155)
		cls.description = String(max=155)
		cls.occurrence = Dict()
		cls.blocked = Boolean()
		cls.settledAt = String(max=155)
		cls.additionalId = Int()
		cls.grossAmount = Int()
		cls.installment = Obj(context=cls, key='installment', name='Installment')
		cls.references = ObjList(context=cls, key='references', name='Reference')
		cls.eventId = String(max=155)
		cls.liquidAmount = Int()
		cls._links = Dict()

		super().__init__(**kw)
