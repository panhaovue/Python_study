import  multiprocessing
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import time
import sys
import numpy as np
x = 15
tiempoG,escalonG,salidaG= [0],[0],[0]
class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4.5, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.axes.set_xscale = 'linear'
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        # FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        # FigureCanvas.updateGeometry(self)

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Simulacion'
        self.width = 900
        self.height = 530
        self.left = 10
        self.top = 40
        self.b0 = 0

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.panel()
        self.b0.clicked.connect(self.hola)
        self.b1.clicked.connect(self.adios)
        self.m = PlotCanvas(self, dpi=80, width=10.4, height=4.2)
        self.m.axes.grid()
        self.m.move(26, 25)

        self.show()


    def panel(self):
        self.b0 = QPushButton('Hola', self)
        self.b0.move(150,450)
        self.b1 = QPushButton('adios', self)
        self.b1.move(300,450)

    @pyqtSlot()
    def hola(self):

        self.P1 = multiprocessing.Process(target=App.f1, args=(self,i))
        self.P2 = multiprocessing.Process(target=self.plot, args = (tiempo, salida, escalon,a))
        a.value, tiempo.value, salida.value, escalon.value = 1, 0, 0, 0
        self.P1.start()
        self.P2.start()

    @pyqtSlot()
    def adios(self):
        a.value = 0
        self.P1.join()
        self.P2.join()

    def plot(self,tiempo,salida,escalon,a):
        global tiempoG,escalonG,salidaG
        while a.value:
            tiempoG = np.append(tiempoG, tiempo.value)
            salidaG = np.append(salidaG, salida.value)
            escalonG = np.append(escalonG, escalon.value)
            self.m.axes.set_ylim(0, 1)
            # Se desabilita el autosacle
            self.m.axes.set_autoscale_on(False)
            # se crean las lineas vacias
            self.m.axes.plot(tiempoG, salidaG, 'r', tiempoG, escalonG, 'b')
            self.m.axes.legend(['Salida', 'Escalon'], shadow=True, fontsize='medium', fancybox='True', loc=1)
            self.m.axes.set_title(u'Control Adaptativo')
            self.m.axes.set_ylabel(u'Amplitud [%]')
            self.m.axes.set_xlabel(u'Tiempo [s]')
            self.m.axes.minorticks_on()
            self.m.draw()
            time.sleep(0.5)


    def f1(self,i):
        global x
        i.value = 0.0
        while 1:
            i.value += 1
            print("i: ", i.value*x)
            time.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    q= multiprocessing.Queue()
    a = multiprocessing.Value('i', 0)
    i = multiprocessing.Value('d', 0.0)
    tiempo = multiprocessing.Value('d',0.0)
    salida = multiprocessing.Value('d', 0.0)
    escalon = multiprocessing.Value('d', 0.0)
    sys.exit(app.exec_())