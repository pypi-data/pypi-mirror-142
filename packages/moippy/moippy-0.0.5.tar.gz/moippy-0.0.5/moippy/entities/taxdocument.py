# -*- coding: utf-8 -*-
from .lib import *

class TaxDocument(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.type = String(max=4)
		cls.number = String(max=16)
		
		super().__init__(**kw)
