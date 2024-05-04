from pade.behaviours.protocols import FipaSubscribeProtocol

from pade.misc.utility import display_message

from pade.acl.messages import ACLMessage

from .data import Root

class PublisherProtocol(FipaSubscribeProtocol):

    def __init__(self, agent):
        super(PublisherProtocol, self).__init__(agent,
                                                   message=None,
                                                   is_initiator=False)

    def handle_subscribe(self, message):
        self.register(message.sender)
        display_message(self.agent.aid.name, '{} from {}'.format(message.content,
                                                                 message.sender.name))
        reply = message.create_reply()
        reply.set_performative(ACLMessage.AGREE)
        reply.set_content('Subscribe message accepted')
        self.agent.send(reply)

    def handle_cancel(self, message):
        self.deregister(self, message.sender)
        display_message(self.agent.aid.name, message.content)

    def notify(self, message):
        super(PublisherProtocol, self).notify(message)

import pickle
class SubscriberProtocol(FipaSubscribeProtocol):

    def __init__(self, agent, message):
        super(SubscriberProtocol, self).__init__(agent,
                                                 message,
                                                 is_initiator=True)

    def handle_agree(self, message):
        display_message(self.agent.aid.name, message.content)

    def handle_inform(self, message):
        data = pickle.loads(message.content)
        display_message(self.agent.aid.name, make_some_calculations(data))

def make_some_calculations(data: Root) -> str:
    return format("Calculated some data: {}".format(data.usd.get('eur')))