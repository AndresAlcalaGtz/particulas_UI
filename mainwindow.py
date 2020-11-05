from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor
from ui_mainwindow import Ui_MainWindow
from laboratorio import Laboratorio
from particula import Particula

class MainWindow(QMainWindow): 

    def __init__(self):
        super(MainWindow, self).__init__()
        self.lab = Laboratorio()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene()
        self.ui.dibujo_graphicsView.setScene(self.scene)
        self.ui.actionAbrir.triggered.connect(self.action_openfile)
        self.ui.actionGuardar.triggered.connect(self.action_savefile)
        self.ui.agregarinicio_pushButton.clicked.connect(self.push_front)
        self.ui.agregarfinal_pushButton.clicked.connect(self.push_back)
        self.ui.mostrar_pushButton.clicked.connect(self.show_all)
        self.ui.mostrartabla_pushButton.clicked.connect(self.show_table)
        self.ui.buscar_pushButton.clicked.connect(self.search_id) 
        self.ui.dibujar_pushButton.clicked.connect(self.draw)
        self.ui.limpiar_pushButton.clicked.connect(self.clear)

    @Slot()
    def action_openfile(self):
        ubicacion = QFileDialog.getOpenFileName(self, "Abrir archivo", ".", "JSON (*.json)")[0]
        if self.lab.abrir(ubicacion):
            QMessageBox.information(self, "Éxito", "Se ha abierto el archivo. " + ubicacion)
        else:
            QMessageBox.critical(self, "Error", "No se ha abierto el archivo. " + ubicacion)

    @Slot()
    def action_savefile(self):
        ubicacion = QFileDialog.getSaveFileName(self, "Guardar archivo", ".", "JSON (*.json)")[0]
        if self.lab.guardar(ubicacion):
            QMessageBox.information(self, "Éxito", "Se pudo crear el archivo. " + ubicacion)
        else:
            QMessageBox.critical(self, "Error", "No se pudo crear el archivo. " + ubicacion)

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
        self.ui.mostrartexto_plainTextEdit.clear()
        self.ui.mostrartexto_plainTextEdit.insertPlainText(str(self.lab))

    def show_row(self, row: int, particle: Particula):
        id_widget = QTableWidgetItem(str(particle.getID))
        origenx_widget = QTableWidgetItem(str(particle.getOrigenX))
        origeny_widget = QTableWidgetItem(str(particle.getOrigenY))
        destinox_widget = QTableWidgetItem(str(particle.getDestinoX))
        destinoy_widget = QTableWidgetItem(str(particle.getDestinoY))
        velocidad_widget = QTableWidgetItem(str(particle.getVelocidad))
        red_widget = QTableWidgetItem(str(particle.getRed))
        green_widget = QTableWidgetItem(str(particle.getGreen))
        blue_widget = QTableWidgetItem(str(particle.getBlue))
        distancia_widget = QTableWidgetItem(str(particle.getDistancia))
        self.ui.tabla_tableWidget.setItem(row, 0, id_widget)
        self.ui.tabla_tableWidget.setItem(row, 1, origenx_widget)
        self.ui.tabla_tableWidget.setItem(row, 2, origeny_widget)
        self.ui.tabla_tableWidget.setItem(row, 3, destinox_widget)
        self.ui.tabla_tableWidget.setItem(row, 4, destinoy_widget)
        self.ui.tabla_tableWidget.setItem(row, 5, velocidad_widget)
        self.ui.tabla_tableWidget.setItem(row, 6, red_widget)
        self.ui.tabla_tableWidget.setItem(row, 7, green_widget)
        self.ui.tabla_tableWidget.setItem(row, 8, blue_widget)
        self.ui.tabla_tableWidget.setItem(row, 9, distancia_widget)

    @Slot()
    def show_table(self):
        headers = ["ID", "Origen (x)", "Origen (y)", "Destino (x)", "Destino (y)", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla_tableWidget.clear()
        self.ui.tabla_tableWidget.setColumnCount(10)
        self.ui.tabla_tableWidget.setHorizontalHeaderLabels(headers)
        self.ui.tabla_tableWidget.setRowCount(len(self.lab))
        r = 0
        for p in self.lab:
            self.show_row(r, p)
            r += 1

    @Slot()
    def search_id(self):
        headers = ["ID", "Origen (x)", "Origen (y)", "Destino (x)", "Destino (y)", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla_tableWidget.clear()
        self.ui.tabla_tableWidget.setColumnCount(10)
        self.ui.tabla_tableWidget.setHorizontalHeaderLabels(headers)
        self.ui.tabla_tableWidget.setRowCount(0)
        searchID = self.ui.buscartexto_lineEdit.text()
        found = False
        for p in self.lab:
            if searchID == str(p.getID):
                self.ui.tabla_tableWidget.setRowCount(1)
                self.show_row(0, p)
                found = True     
        if not found:
            QMessageBox.warning(self, 'Atención', f'La partícula con la ID "{searchID}" no fue encontrada')

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.dibujo_graphicsView.scale(1.2, 1.2)
        else:
            self.ui.dibujo_graphicsView.scale(0.8, 0.8)

    @Slot()
    def draw(self):
        pen = QPen()
        pen.setWidth(2)
        for p in self.lab:
            color = QColor(p.getRed, p.getGreen, p.getBlue)
            pen.setColor(color)
            self.scene.addEllipse(p.getOrigenX, p.getOrigenY, 3, 3, pen)
            self.scene.addEllipse(p.getDestinoX, p.getDestinoY, 3, 3, pen)
            self.scene.addLine(p.getOrigenX+3, p.getOrigenY+1, p.getDestinoX, p.getDestinoY+1, pen)

    @Slot()
    def clear(self):
        self.scene.clear()