# -*- coding: utf-8 -*-
from .lib import *

class Geolocation(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.latitude = Float()
		cls.longitude = Float()


		super().__init__(**kw)
