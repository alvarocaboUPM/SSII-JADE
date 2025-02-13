from pade.core.agent import Agent

from pade.acl.messages import ACLMessage

from pade.acl.aid import AID

from gui.gui import MainWindow

from .fetch_behaviour import FetchBehaviour

from .protocols import PublisherProtocol, SubscriberProtocol
from .data import API
from pade.acl.messages import ACLMessage

from pade.core.agent import Agent

class AgentPublisher(Agent):
    """
    Represents a publisher agent.

    Args:
        aid (str): The unique identifier for the agent.

    Attributes:
        protocol (PublisherProtocol): The protocol used by the agent.
        self.timed_behaviour = Time(self, self.protocol.notify)
        (Time): The timed behavior of the agent.
        behaviours (list): The list of behaviors of the agent.

    """

    def __init__(self, aid, api: API):
        super(AgentPublisher, self).__init__(aid)

        self.protocol = PublisherProtocol(self)
        self.timed_behaviour = FetchBehaviour(self, self.protocol.notify, api)
        self.behaviours.append(self.protocol)
        self.behaviours.append(self.timed_behaviour)

class AgentSubscriber(Agent):
    """
    Represents a subscriber agent that can launch a subscriber protocol.

    Args:
        aid (str): The unique identifier of the agent.
        receiver_aid (AID): The AID of the receiver agent.

    Attributes:
        protocol (SubscriberProtocol): The subscriber protocol associated with the agent.

    """

    def __init__(self, aid, receiver_aid: AID, window: MainWindow):
        """
        Initializes an instance of the AgentSubscriber class.

        Args:
            aid (str): The identifier of the agent.
            receiver_aid (AID): The identifier of the receiver agent.

        """
        super(AgentSubscriber, self).__init__(aid)

        self.call_later(8.0, self.launch_subscriber_protocol, receiver_aid, window)

    def launch_subscriber_protocol(self, aid: AID, window: MainWindow):
        """
        Launches the subscriber protocol.

        Args:
            aid (AID): The AID of the receiver agent.

        """
        msg = ACLMessage(ACLMessage.SUBSCRIBE)
        msg.set_protocol(ACLMessage.FIPA_SUBSCRIBE_PROTOCOL)
        msg.set_content('Subscription request')
        msg.add_receiver(aid)

        self.protocol = SubscriberProtocol(self, msg, window)
        self.behaviours.append(self.protocol)
        self.protocol.on_start()

    def on_start(self):
        return super().on_start()