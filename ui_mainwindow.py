# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(779, 539)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pestanas_tabWidget = QTabWidget(self.centralwidget)
        self.pestanas_tabWidget.setObjectName(u"pestanas_tabWidget")
        self.agregar_tab = QWidget()
        self.agregar_tab.setObjectName(u"agregar_tab")
        self.gridLayout_2 = QGridLayout(self.agregar_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.agregar_groupBox = QGroupBox(self.agregar_tab)
        self.agregar_groupBox.setObjectName(u"agregar_groupBox")
        self.agregar_groupBox.setInputMethodHints(Qt.ImhNone)
        self.gridLayout = QGridLayout(self.agregar_groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.velocidad_spinBox = QSpinBox(self.agregar_groupBox)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")
        self.velocidad_spinBox.setMaximum(999999999)

        self.gridLayout.addWidget(self.velocidad_spinBox, 5, 1, 1, 1)

        self.ordenardistancia_pushButton = QPushButton(self.agregar_groupBox)
        self.ordenardistancia_pushButton.setObjectName(u"ordenardistancia_pushButton")

        self.gridLayout.addWidget(self.ordenardistancia_pushButton, 12, 0, 1, 2)

        self.green_label = QLabel(self.agregar_groupBox)
        self.green_label.setObjectName(u"green_label")

        self.gridLayout.addWidget(self.green_label, 7, 0, 1, 1)

        self.ordenarvelocidad_pushButton = QPushButton(self.agregar_groupBox)
        self.ordenarvelocidad_pushButton.setObjectName(u"ordenarvelocidad_pushButton")

        self.gridLayout.addWidget(self.ordenarvelocidad_pushButton, 13, 0, 1, 2)

        self.origeny_spinBox = QSpinBox(self.agregar_groupBox)
        self.origeny_spinBox.setObjectName(u"origeny_spinBox")
        self.origeny_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origeny_spinBox, 2, 1, 1, 1)

        self.destinox_label = QLabel(self.agregar_groupBox)
        self.destinox_label.setObjectName(u"destinox_label")

        self.gridLayout.addWidget(self.destinox_label, 3, 0, 1, 1)

        self.velocidad_label = QLabel(self.agregar_groupBox)
        self.velocidad_label.setObjectName(u"velocidad_label")

        self.gridLayout.addWidget(self.velocidad_label, 5, 0, 1, 1)

        self.ordenarid_pushButton = QPushButton(self.agregar_groupBox)
        self.ordenarid_pushButton.setObjectName(u"ordenarid_pushButton")

        self.gridLayout.addWidget(self.ordenarid_pushButton, 11, 0, 1, 2)

        self.blue_spinBox = QSpinBox(self.agregar_groupBox)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.blue_spinBox, 8, 1, 1, 1)

        self.blue_label = QLabel(self.agregar_groupBox)
        self.blue_label.setObjectName(u"blue_label")

        self.gridLayout.addWidget(self.blue_label, 8, 0, 1, 1)

        self.origenx_label = QLabel(self.agregar_groupBox)
        self.origenx_label.setObjectName(u"origenx_label")

        self.gridLayout.addWidget(self.origenx_label, 1, 0, 1, 1)

        self.green_spinBox = QSpinBox(self.agregar_groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.green_spinBox, 7, 1, 1, 1)

        self.mostrartexto_pushButton = QPushButton(self.agregar_groupBox)
        self.mostrartexto_pushButton.setObjectName(u"mostrartexto_pushButton")

        self.gridLayout.addWidget(self.mostrartexto_pushButton, 14, 0, 1, 2)

        self.destinoy_spinBox = QSpinBox(self.agregar_groupBox)
        self.destinoy_spinBox.setObjectName(u"destinoy_spinBox")
        self.destinoy_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinoy_spinBox, 4, 1, 1, 1)

        self.origeny_label = QLabel(self.agregar_groupBox)
        self.origeny_label.setObjectName(u"origeny_label")

        self.gridLayout.addWidget(self.origeny_label, 2, 0, 1, 1)

        self.origenx_spinBox = QSpinBox(self.agregar_groupBox)
        self.origenx_spinBox.setObjectName(u"origenx_spinBox")
        self.origenx_spinBox.setAutoFillBackground(False)
        self.origenx_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origenx_spinBox, 1, 1, 1, 1)

        self.destinoy_label = QLabel(self.agregar_groupBox)
        self.destinoy_label.setObjectName(u"destinoy_label")

        self.gridLayout.addWidget(self.destinoy_label, 4, 0, 1, 1)

        self.red_spinBox = QSpinBox(self.agregar_groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.red_spinBox, 6, 1, 1, 1)

        self.agregarinicio_pushButton = QPushButton(self.agregar_groupBox)
        self.agregarinicio_pushButton.setObjectName(u"agregarinicio_pushButton")

        self.gridLayout.addWidget(self.agregarinicio_pushButton, 9, 0, 1, 2)

        self.red_label = QLabel(self.agregar_groupBox)
        self.red_label.setObjectName(u"red_label")

        self.gridLayout.addWidget(self.red_label, 6, 0, 1, 1)

        self.id_spinBox = QSpinBox(self.agregar_groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")
        self.id_spinBox.setMaximum(999999999)

        self.gridLayout.addWidget(self.id_spinBox, 0, 1, 1, 1)

        self.agregarfinal_pushButton = QPushButton(self.agregar_groupBox)
        self.agregarfinal_pushButton.setObjectName(u"agregarfinal_pushButton")

        self.gridLayout.addWidget(self.agregarfinal_pushButton, 10, 0, 1, 2)

        self.destinox_spinBox = QSpinBox(self.agregar_groupBox)
        self.destinox_spinBox.setObjectName(u"destinox_spinBox")
        self.destinox_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinox_spinBox, 3, 1, 1, 1)

        self.id_label = QLabel(self.agregar_groupBox)
        self.id_label.setObjectName(u"id_label")

        self.gridLayout.addWidget(self.id_label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.agregar_groupBox, 0, 0, 1, 1)

        self.mostrartexto_plainTextEdit = QPlainTextEdit(self.agregar_tab)
        self.mostrartexto_plainTextEdit.setObjectName(u"mostrartexto_plainTextEdit")

        self.gridLayout_2.addWidget(self.mostrartexto_plainTextEdit, 0, 1, 1, 1)

        self.pestanas_tabWidget.addTab(self.agregar_tab, "")
        self.tabla_tab = QWidget()
        self.tabla_tab.setObjectName(u"tabla_tab")
        self.gridLayout_4 = QGridLayout(self.tabla_tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabla_tableWidget = QTableWidget(self.tabla_tab)
        self.tabla_tableWidget.setObjectName(u"tabla_tableWidget")

        self.gridLayout_4.addWidget(self.tabla_tableWidget, 0, 0, 1, 3)

        self.buscartexto_lineEdit = QLineEdit(self.tabla_tab)
        self.buscartexto_lineEdit.setObjectName(u"buscartexto_lineEdit")

        self.gridLayout_4.addWidget(self.buscartexto_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tabla_tab)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_4.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.mostrartabla_pushButton = QPushButton(self.tabla_tab)
        self.mostrartabla_pushButton.setObjectName(u"mostrartabla_pushButton")

        self.gridLayout_4.addWidget(self.mostrartabla_pushButton, 1, 2, 1, 1)

        self.pestanas_tabWidget.addTab(self.tabla_tab, "")
        self.dibujar_tab = QWidget()
        self.dibujar_tab.setObjectName(u"dibujar_tab")
        self.gridLayout_5 = QGridLayout(self.dibujar_tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.dibujo_graphicsView = QGraphicsView(self.dibujar_tab)
        self.dibujo_graphicsView.setObjectName(u"dibujo_graphicsView")

        self.gridLayout_5.addWidget(self.dibujo_graphicsView, 0, 0, 1, 2)

        self.dibujar_pushButton = QPushButton(self.dibujar_tab)
        self.dibujar_pushButton.setObjectName(u"dibujar_pushButton")

        self.gridLayout_5.addWidget(self.dibujar_pushButton, 1, 0, 1, 1)

        self.limpiar_pushButton = QPushButton(self.dibujar_tab)
        self.limpiar_pushButton.setObjectName(u"limpiar_pushButton")

        self.gridLayout_5.addWidget(self.limpiar_pushButton, 1, 1, 1, 1)

        self.pestanas_tabWidget.addTab(self.dibujar_tab, "")
        self.grafo_tab = QWidget()
        self.grafo_tab.setObjectName(u"grafo_tab")
        self.gridLayout_7 = QGridLayout(self.grafo_tab)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.grafo_groupBox = QGroupBox(self.grafo_tab)
        self.grafo_groupBox.setObjectName(u"grafo_groupBox")
        self.grafo_groupBox.setMaximumSize(QSize(300, 16777215))
        self.gridLayout_6 = QGridLayout(self.grafo_groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.amplitud_pushButton = QPushButton(self.grafo_groupBox)
        self.amplitud_pushButton.setObjectName(u"amplitud_pushButton")

        self.gridLayout_6.addWidget(self.amplitud_pushButton, 4, 0, 1, 2)

        self.x_label = QLabel(self.grafo_groupBox)
        self.x_label.setObjectName(u"x_label")

        self.gridLayout_6.addWidget(self.x_label, 0, 0, 1, 1)

        self.y_label = QLabel(self.grafo_groupBox)
        self.y_label.setObjectName(u"y_label")

        self.gridLayout_6.addWidget(self.y_label, 1, 0, 1, 1)

        self.profundidad_pushButton = QPushButton(self.grafo_groupBox)
        self.profundidad_pushButton.setObjectName(u"profundidad_pushButton")

        self.gridLayout_6.addWidget(self.profundidad_pushButton, 3, 0, 1, 2)

        self.x_spinBox = QSpinBox(self.grafo_groupBox)
        self.x_spinBox.setObjectName(u"x_spinBox")
        self.x_spinBox.setMaximum(999999999)

        self.gridLayout_6.addWidget(self.x_spinBox, 0, 1, 1, 1)

        self.mostrargrafo_pushButton = QPushButton(self.grafo_groupBox)
        self.mostrargrafo_pushButton.setObjectName(u"mostrargrafo_pushButton")

        self.gridLayout_6.addWidget(self.mostrargrafo_pushButton, 2, 0, 1, 2)

        self.y_spinBox = QSpinBox(self.grafo_groupBox)
        self.y_spinBox.setObjectName(u"y_spinBox")
        self.y_spinBox.setMaximum(999999999)

        self.gridLayout_6.addWidget(self.y_spinBox, 1, 1, 1, 1)


        self.gridLayout_7.addWidget(self.grafo_groupBox, 0, 0, 1, 1)

        self.grafo_graphicsView = QGraphicsView(self.grafo_tab)
        self.grafo_graphicsView.setObjectName(u"grafo_graphicsView")

        self.gridLayout_7.addWidget(self.grafo_graphicsView, 0, 1, 2, 1)

        self.operaciongrafo_plainTextEdit = QPlainTextEdit(self.grafo_tab)
        self.operaciongrafo_plainTextEdit.setObjectName(u"operaciongrafo_plainTextEdit")
        self.operaciongrafo_plainTextEdit.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_7.addWidget(self.operaciongrafo_plainTextEdit, 1, 0, 2, 1)

        self.listas_plainTextEdit = QPlainTextEdit(self.grafo_tab)
        self.listas_plainTextEdit.setObjectName(u"listas_plainTextEdit")
        self.listas_plainTextEdit.setMaximumSize(QSize(16777215, 150))

        self.gridLayout_7.addWidget(self.listas_plainTextEdit, 2, 1, 1, 1)

        self.pestanas_tabWidget.addTab(self.grafo_tab, "")

        self.gridLayout_3.addWidget(self.pestanas_tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 779, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.pestanas_tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Laboratorio de particulas", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.agregar_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edcula", None))
        self.ordenardistancia_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar part\u00edculas (Distancia - descendente)", None))
        self.green_label.setText(QCoreApplication.translate("MainWindow", u"Color (Green):", None))
        self.ordenarvelocidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar part\u00edculas (Velocidad - ascendente)", None))
        self.destinox_label.setText(QCoreApplication.translate("MainWindow", u"Destino (x):", None))
        self.velocidad_label.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.ordenarid_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar part\u00edculas (ID - ascendente)", None))
        self.blue_label.setText(QCoreApplication.translate("MainWindow", u"Color (Blue):", None))
        self.origenx_label.setText(QCoreApplication.translate("MainWindow", u"Origen (x):", None))
        self.mostrartexto_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar part\u00edculas", None))
        self.origeny_label.setText(QCoreApplication.translate("MainWindow", u"Origen (y):", None))
        self.destinoy_label.setText(QCoreApplication.translate("MainWindow", u"Destino (y):", None))
        self.agregarinicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar part\u00edcula al inicio", None))
        self.red_label.setText(QCoreApplication.translate("MainWindow", u"Color (Red):", None))
        self.agregarfinal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar part\u00edcula al final", None))
        self.id_label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.pestanas_tabWidget.setTabText(self.pestanas_tabWidget.indexOf(self.agregar_tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscartexto_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID de la part\u00edcula", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrartabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.pestanas_tabWidget.setTabText(self.pestanas_tabWidget.indexOf(self.tabla_tab), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.pestanas_tabWidget.setTabText(self.pestanas_tabWidget.indexOf(self.dibujar_tab), QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.grafo_groupBox.setTitle("")
        self.amplitud_pushButton.setText(QCoreApplication.translate("MainWindow", u"Busqueda en amplitud", None))
        self.x_label.setText(QCoreApplication.translate("MainWindow", u"Origen (x):", None))
        self.y_label.setText(QCoreApplication.translate("MainWindow", u"Origen (y):", None))
        self.profundidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"Busqueda en profundidad", None))
        self.mostrargrafo_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar grafo", None))
        self.pestanas_tabWidget.setTabText(self.pestanas_tabWidget.indexOf(self.grafo_tab), QCoreApplication.translate("MainWindow", u"Grafo", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

