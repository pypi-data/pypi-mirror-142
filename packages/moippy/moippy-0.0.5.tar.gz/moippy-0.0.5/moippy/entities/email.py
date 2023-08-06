# -*- coding: utf-8 -*-
from .lib import *

class Email(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.address = String(max=255)
		cls.confirmed = Boolean()

		super().__init__(**kw)
