# -*- coding: utf-8 -*-
from .lib import *

class Device(MoipEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.ip = String(max=55)
		cls.geolocation = Obj(context=cls, key='geolocation', name='Geolocation')
		cls.userAgent = String(max=555)


		super().__init__(**kw)
