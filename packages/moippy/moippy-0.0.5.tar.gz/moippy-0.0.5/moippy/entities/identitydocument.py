# -*- coding: utf-8 -*-
from .lib import *

class IdentityDocument(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.number = String(max=55)
		cls.issuer = String(max=16)
		cls.issueDate = DateTime(format="%Y-%m-%d")
		cls.type = String(max=16)
