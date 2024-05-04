
from pade.misc.utility import start_loop
from pade.acl.aid import AID
from sys import argv

from flask import Flask
from models.agents import AgentPublisher, AgentSubscriber


def generate_agents() -> list:
    agents_per_process = 1
    c = 0
    agents = list()
    for i in range(agents_per_process):
        port = int(argv[1]) + c
        k = 10000
        participants = list()

        agent_name = 'agent_publisher_{}@localhost:{}'.format(port, port)
        participants.append(agent_name)
        agent_pub_1 = AgentPublisher(AID(name=agent_name))
        agents.append(agent_pub_1)

        agent_name = 'agent_subscriber_{}@localhost:{}'.format(port + k, port + k)
        participants.append(agent_name)
        agent_sub_1 = AgentSubscriber(AID(name=agent_name), agent_pub_1.aid)
        agents.append(agent_sub_1)

        agent_name = 'agent_subscriber_{}@localhost:{}'.format(port - k, port - k)
        agent_sub_2 = AgentSubscriber(AID(name=agent_name), agent_pub_1.aid)
        agents.append(agent_sub_2)

        c += 1000
    return agents

def start_up_flask():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Hello World'

    app.run(port=5001)

if __name__ == '__main__':
    #start_up_flask()
    start_loop(generate_agents())
