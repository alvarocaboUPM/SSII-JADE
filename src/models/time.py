
import random
from pade.acl.messages import ACLMessage

from pade.behaviours.protocols import TimedBehaviour

from pade.core.agent import Agent

class Time(TimedBehaviour):

    def __init__(self, agent: Agent, notify):
        super(Time, self).__init__(agent, 1)
        self.notify = notify
        self.inc = 0

    def on_time(self):
        super(Time, self).on_time()
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_SUBSCRIBE_PROTOCOL)
        # message.set_content("Hola subscritores, el tiempo es: {}".format(self.inc))
        message.set_content(random.random())
        self.notify(message)
        self.inc += 0.1