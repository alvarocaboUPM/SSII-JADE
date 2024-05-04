
import requests as req

from pade.acl.messages import ACLMessage
from pade.behaviours.protocols import TimedBehaviour
from pade.core.agent import Agent

class AgentFetcher(TimedBehaviour):
    """_summary_
        Fetches data from an API once a second.
    Args:
        TimedBehaviour (_type_): _description_
    """

    def __init__(self, agent: Agent, notify):
        super(AgentFetcher, self).__init__(agent, 1)
        self.notify = notify
        self.data = 0
        self.url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date}/{apiVersion}/{endpoint}"

    def on_time(self):
        super(AgentFetcher, self).on_time()
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_SUBSCRIBE_PROTOCOL)
        self.data = self.fetch()
        message.set_content(self.data)
        self.notify(message)

    def fetch(self):
        formatted_url = self.url.format(date="latest", apiVersion="v1", endpoint="currencies/usd.json")
        response = req.get(formatted_url)

        if response.status_code != 200:
            return None

        values = response.json().get("usd")
        return values.get("vef")
