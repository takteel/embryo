from action import Action
from callback import Callback

action = Action(name='action_0')
action.save()

cb_0 = Callback(name='cb_0', action=action, index=0)
cb_1 = Callback(name='cb_1', action=action, index=1)
cb_3 = Callback(name='cb_3', action=action, index=3)
cb_2 = Callback(name='cb_2', action=action, index=2)

cb_0.save()
cb_1.save()
cb_3.save()
cb_2.save()

action.run()
action.delete()
