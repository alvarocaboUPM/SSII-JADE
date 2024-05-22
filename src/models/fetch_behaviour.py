
import pickle

from pade.acl.messages import ACLMessage
from pade.behaviours.protocols import TimedBehaviour
from pade.core.agent import Agent

from .data import RandomNumberAPI, API

class FetchBehaviour(TimedBehaviour):
    """_summary_
        Fetches data from an API once a second.
    Args:
        TimedBehaviour (_type_): _description_
    """

    def __init__(self, agent: Agent, notify, api: API):
        super(FetchBehaviour, self).__init__(agent, 1)
        self.notify = notify
        self.data = 0
        self.api = api

    def on_time(self):
        super(FetchBehaviour, self).on_time()
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_SUBSCRIBE_PROTOCOL)
        #Fetches the data from a source
        self.data = self.api.fetch()
        # Serialize the data
        message.set_content(pickle.dumps(self.data)) 
        #Send the data to the subscribers
        self.notify(message)
