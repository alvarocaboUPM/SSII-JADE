from PyQt5.QtWidgets import QApplication
import sys
from pade.misc.utility import start_loop
from pade.acl.aid import AID
from sys import argv

from flask import Flask
from models.agents import AgentPublisher, AgentSubscriber
from gui.gui import MainWindow
import threading

from models.data import RandomNumberAPI, API


def generate_agents(window: MainWindow, api: API) -> list:
    agents_per_process = 1
    c = 0
    agents = list()
    for _ in range(agents_per_process):
        port = int(argv[1]) + c
        k = 10000
        participants = list()

        agent_name = 'agent_publisher_{}@localhost:{}'.format(port, port)
        participants.append(agent_name)
        agent_pub_1 = AgentPublisher(AID(name=agent_name), api)
        agents.append(agent_pub_1)

        agent_name = 'agent_subscriber_{}@localhost:{}'.format(port + k, port + k)
        participants.append(agent_name)
        agent_sub_1 = AgentSubscriber(AID(name=agent_name), agent_pub_1.aid, window)
        agents.append(agent_sub_1)

        agent_name = 'agent_subscriber_{}@localhost:{}'.format(port - k, port - k)
        agent_sub_2 = AgentSubscriber(AID(name=agent_name), agent_pub_1.aid, window)
        agents.append(agent_sub_2)

        c += 1000
    return agents

if __name__ == '__main__':
    api = RandomNumberAPI()
    app = QApplication(sys.argv)
    window = MainWindow(api)
    threading.Thread(target=start_loop, args=(generate_agents(window,api),)).start()
    window.show()
    sys.exit(app.exec_())
