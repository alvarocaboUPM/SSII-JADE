from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

from models.data import API,RandomNumberAPI

class MainWindow(QMainWindow):
    def __init__(self, api: API = RandomNumberAPI()):
        super().__init__()

        self.setWindowTitle("Live Data Plot")
        self.setGeometry(100, 100, 800, 600)

        self.y: list[float] = []

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.layout.addWidget(self.canvas)

        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel(api.xLabel)
        self.ax.set_ylabel(api.yLabel)
        self.ax.set_title(api.title)

    def update_plot(self, data: float):
        self.ax.clear()
        self.y.append(data)
        x = np.arange(len(self.y))
        self.ax.plot(x, self.y, 'r-')
        self.canvas.draw()


