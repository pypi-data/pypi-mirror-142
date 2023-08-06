# -*- coding: utf-8 -*-
from .lib import *

class Boleto(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=55)
		cls.expirationDate = DateTime()
		cls.instructionLines = Obj(context=cls, key='instructionLines', name='InstructionLine')
		cls.logoUri = String(max=255)

		super().__init__(**kw)
