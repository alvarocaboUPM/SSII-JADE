from pade.core.agent import Agent

from pade.acl.messages import ACLMessage

from pade.acl.aid import AID

from .protocols import PublisherProtocol, SubscriberProtocol
from .time import Time




class AgentPublisher(Agent):

    def __init__(self, aid):
        super(AgentPublisher, self).__init__(aid)

        self.protocol = PublisherProtocol(self)
        self.timed = Time(self, self.protocol.notify)

        self.behaviours.append(self.protocol)
        self.behaviours.append(self.timed)

class AgentSubscriber(Agent):

    def __init__(self, aid, receiver_aid: AID):
        super(AgentSubscriber, self).__init__(aid)

        self.call_later(8.0, self.launch_subscriber_protocol, receiver_aid)

    def launch_subscriber_protocol(self, aid: AID):
        msg = ACLMessage(ACLMessage.SUBSCRIBE)
        msg.set_protocol(ACLMessage.FIPA_SUBSCRIBE_PROTOCOL)
        msg.set_content('Subscription request')
        msg.add_receiver(aid)

        self.protocol = SubscriberProtocol(self, msg)
        self.behaviours.append(self.protocol)
        self.protocol.on_start()
