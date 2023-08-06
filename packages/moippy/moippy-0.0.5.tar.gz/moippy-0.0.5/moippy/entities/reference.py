# -*- coding: utf-8 -*-
from .lib import *

class Reference(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.value = String(max=255)
		cls.type = String(max=255)

		super().__init__(**kw)
