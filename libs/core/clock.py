from datetime import datetime
from django.utils.timezone import utc

class Clock(object):
	@staticmethod
	def now():
		return datetime.utcnow().replace(tzinfo=utc)
