from libs.core.clock import Clock
import models

from threading import Thread, Event

class ActionProcessor(object):
	def __init__(self, *args, **kwargs):
		super(ActionProcessor, self).__init__(*args, **kwargs)

		self.__mustStop = False
		self.__event = Event()
		self.__event.set()
		self.__thread = Thread(target=self.waitActions, name="carbon:actions processor")
		self.__maxSleepDelay = 60.0
		self.__nextActionDelay = 60.0
		
	def queryNextActions(self):
		now = Clock.now()

		allActions = models.Action.objects.order_by('completion_time')
		passedActions = allActions.filter(completion_time__lte=now)
		nextActions = allActions.exclude(completion_time__lte=now)

		return passedActions, nextActions[0] if len(nextActions) > 0 else None

	def waitActions(self):
		while not self.__mustStop:
			sleepDuration = min(max(self.__nextActionDelay, 0.0), self.__maxSleepDelay)
			
			print "waiting"
			eventIsSet = self.__event.wait(sleepDuration)

			if eventIsSet:
				print "event set"
				self.__event.clear()
			else:  # timeout
				print "timeout"
				self.__nextActionDelay = self.__maxSleepDelay

			passedActions, nextAction = self.queryNextActions()

			for action in passedActions:
				print "processing ", action
				action.run()
				action.delete()				
				
			if nextAction:
				actionDelay = (nextAction.completion_time - Clock.now()).total_seconds()
				self.__nextActionDelay = min(actionDelay, self.__nextActionDelay)

	def start(self):
		self.__thread.start()
		
	def stop(self):
		self.__mustStop = True
		self.__event.set()
		self.__thread.join()

	def notify(self, cls=None, instance=None):
		self.__event.set()
		self.__nextActionDelay = min((instance.completion_time - Clock.now()).total_seconds(), self.__nextActionDelay, self.__maxSleepDelay)

singleton = ActionProcessor()
