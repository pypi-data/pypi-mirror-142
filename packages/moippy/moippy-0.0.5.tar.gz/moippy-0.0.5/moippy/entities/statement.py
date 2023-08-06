# -*- coding: utf-8 -*-
from .lib import *

class Statement(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.amount = Int()
		cls.description = String(max=255)
		cls.type = Int()
		cls.date = String(max=155)
		cls._links = Dict()

		super().__init__(**kw)
