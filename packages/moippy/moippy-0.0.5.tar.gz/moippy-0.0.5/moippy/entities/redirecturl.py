# -*- coding: utf-8 -*-
from .lib import *

class RedirectUrl(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.urlSuccess = String(max=255)
		cls.urlFailure = String(max=255)

		super().__init__(**kw)
