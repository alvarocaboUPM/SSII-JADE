from time import sleep
from pade.behaviours.protocols import FipaSubscribeProtocol

from pade.misc.utility import display_message

from pade.acl.messages import ACLMessage

from gui.gui import MainWindow

from .data import ApiResult, Currency

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

    def __init__(self, agent, message, window: MainWindow, update_frecuency=0):
        super(SubscriberProtocol, self).__init__(agent,
                                                 message,
                                                 is_initiator=True)
        self.window = window
        self.update_frecuency = update_frecuency

    def handle_agree(self, message):
        display_message(self.agent.aid.name, message.content)

    def handle_inform(self, message):
        result: ApiResult = pickle.loads(message.content)
        data = result.get_data()
        display_message(self.agent.aid.name, data)
        self.window.update_plot(data)
        if (self.update_frecuency and self.update_frecuency > 0):
            sleep(self.update_frecuency)