from django.db import models

from .action import Action

class Callback(models.Model):
	name = models.CharField(max_length=64)

	index = models.PositiveSmallIntegerField()
	action = models.ForeignKey(Action, related_name="callbacks")

	def __init__(self, *args, **kwargs):
		super(Callback, self).__init__(*args, **kwargs)

	def run(self, *args, **kwargs):
		print self.name, '(', ')'

	class Meta:
		app_label = "defer"
