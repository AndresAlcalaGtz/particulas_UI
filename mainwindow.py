from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from laboratorio import Laboratorio
from particula import Particula

class MainWindow(QMainWindow):


    def __init__(self):
        super(MainWindow, self).__init__()
        self.lab = Laboratorio()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregarinicio_pushButton.clicked.connect(self.push_front)
        self.ui.agregarfinal_pushButton.clicked.connect(self.push_back)
        self.ui.mostrar_pushButton.clicked.connect(self.show_all)


    @Slot()
    def push_front(self):

        ID = self.ui.id_spinBox.value()
        origenX = self.ui.origenx_spinBox.value()
        origenY = self.ui.origeny_spinBox.value()
        destinoX = self.ui.destinox_spinBox.value()
        destinoY = self.ui.destinoy_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        p = Particula(ID, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue)
        self.lab.agregar_inicio(p)


    @Slot()
    def push_back(self):
        
        ID = self.ui.id_spinBox.value()
        origenX = self.ui.origenx_spinBox.value()
        origenY = self.ui.origeny_spinBox.value()
        destinoX = self.ui.destinox_spinBox.value()
        destinoY = self.ui.destinoy_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        p = Particula(ID, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue)
        self.lab.agregar_final(p)

    
    @Slot()
    def show_all(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.lab))