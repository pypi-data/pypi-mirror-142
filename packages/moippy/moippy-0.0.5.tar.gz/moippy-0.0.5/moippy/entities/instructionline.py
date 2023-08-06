# -*- coding: utf-8 -*-
from .lib import *

class InstructionLine(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.first = String(max=150)
		cls.second = String(max=150)
		cls.third = String(max=150)

		super().__init__(**kw)
