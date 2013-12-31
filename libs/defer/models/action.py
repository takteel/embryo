from django.db import models

from libs.core import Clock

class Action(models.Model):
	name = models.CharField(max_length=64)

	creation_time = models.DateTimeField(default=Clock.now)
	start_time = models.DateTimeField(default=Clock.now)
	completion_time = models.DateTimeField(default=Clock.now)

	def __init__(self, *args, **kwargs):
		super(Action, self).__init__(*args, **kwargs)

	def run(self, *args, **kwargs):
		print self.name, '(', ')'
		callbacks = self.callbacks.all().order_by('index')

		for callback in callbacks:
			callback.run(*args, **kwargs)
			callback.delete()

	class Meta:
		app_label = "defer"
