# -*- coding: utf-8 -*-
from .lib import *

class CancellationDetails(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=55)
		cls.cancelledBy = String(max=155)
		cls.description = String(max=155)
		cls.code = String(max=255)

		super().__init__(**kw)
