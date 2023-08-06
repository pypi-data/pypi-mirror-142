# -*- coding: utf-8 -*-
from .lib import *

class Installment(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.addition = Int()
		cls.quantity = Dict()
		cls.amount = Int()
		cls.number = Int()

		super().__init__(**kw)
