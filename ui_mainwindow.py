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
        MainWindow.resize(583, 516)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setInputMethodHints(Qt.ImhNone)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.id_label = QLabel(self.groupBox)
        self.id_label.setObjectName(u"id_label")

        self.gridLayout.addWidget(self.id_label, 0, 0, 1, 1)

        self.id_spinBox = QSpinBox(self.groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")
        self.id_spinBox.setMaximum(999999999)

        self.gridLayout.addWidget(self.id_spinBox, 0, 1, 1, 1)

        self.origenx_label = QLabel(self.groupBox)
        self.origenx_label.setObjectName(u"origenx_label")

        self.gridLayout.addWidget(self.origenx_label, 1, 0, 1, 1)

        self.origenx_spinBox = QSpinBox(self.groupBox)
        self.origenx_spinBox.setObjectName(u"origenx_spinBox")
        self.origenx_spinBox.setAutoFillBackground(False)
        self.origenx_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origenx_spinBox, 1, 1, 1, 1)

        self.origeny_label = QLabel(self.groupBox)
        self.origeny_label.setObjectName(u"origeny_label")

        self.gridLayout.addWidget(self.origeny_label, 2, 0, 1, 1)

        self.origeny_spinBox = QSpinBox(self.groupBox)
        self.origeny_spinBox.setObjectName(u"origeny_spinBox")
        self.origeny_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origeny_spinBox, 2, 1, 1, 1)

        self.destinox_label = QLabel(self.groupBox)
        self.destinox_label.setObjectName(u"destinox_label")

        self.gridLayout.addWidget(self.destinox_label, 3, 0, 1, 1)

        self.destinox_spinBox = QSpinBox(self.groupBox)
        self.destinox_spinBox.setObjectName(u"destinox_spinBox")
        self.destinox_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinox_spinBox, 3, 1, 1, 1)

        self.destinoy_label = QLabel(self.groupBox)
        self.destinoy_label.setObjectName(u"destinoy_label")

        self.gridLayout.addWidget(self.destinoy_label, 4, 0, 1, 1)

        self.destinoy_spinBox = QSpinBox(self.groupBox)
        self.destinoy_spinBox.setObjectName(u"destinoy_spinBox")
        self.destinoy_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinoy_spinBox, 4, 1, 1, 1)

        self.velocidad_label = QLabel(self.groupBox)
        self.velocidad_label.setObjectName(u"velocidad_label")

        self.gridLayout.addWidget(self.velocidad_label, 5, 0, 1, 1)

        self.velocidad_spinBox = QSpinBox(self.groupBox)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")
        self.velocidad_spinBox.setMaximum(999999999)

        self.gridLayout.addWidget(self.velocidad_spinBox, 5, 1, 1, 1)

        self.red_label = QLabel(self.groupBox)
        self.red_label.setObjectName(u"red_label")

        self.gridLayout.addWidget(self.red_label, 6, 0, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.red_spinBox, 6, 1, 1, 1)

        self.green_label = QLabel(self.groupBox)
        self.green_label.setObjectName(u"green_label")

        self.gridLayout.addWidget(self.green_label, 7, 0, 1, 1)

        self.green_spinBox = QSpinBox(self.groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.green_spinBox, 7, 1, 1, 1)

        self.blue_label = QLabel(self.groupBox)
        self.blue_label.setObjectName(u"blue_label")

        self.gridLayout.addWidget(self.blue_label, 8, 0, 1, 1)

        self.blue_spinBox = QSpinBox(self.groupBox)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.blue_spinBox, 8, 1, 1, 1)

        self.agregarinicio_pushButton = QPushButton(self.groupBox)
        self.agregarinicio_pushButton.setObjectName(u"agregarinicio_pushButton")

        self.gridLayout.addWidget(self.agregarinicio_pushButton, 9, 0, 1, 2)

        self.agregarfinal_pushButton = QPushButton(self.groupBox)
        self.agregarfinal_pushButton.setObjectName(u"agregarfinal_pushButton")

        self.gridLayout.addWidget(self.agregarfinal_pushButton, 10, 0, 1, 2)

        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout.addWidget(self.mostrar_pushButton, 11, 0, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 583, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edcula", None))
        self.id_label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.origenx_label.setText(QCoreApplication.translate("MainWindow", u"Origen (x):", None))
        self.origeny_label.setText(QCoreApplication.translate("MainWindow", u"Origen (y):", None))
        self.destinox_label.setText(QCoreApplication.translate("MainWindow", u"Destino (x):", None))
        self.destinoy_label.setText(QCoreApplication.translate("MainWindow", u"Destino (y):", None))
        self.velocidad_label.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.red_label.setText(QCoreApplication.translate("MainWindow", u"Color (Red):", None))
        self.green_label.setText(QCoreApplication.translate("MainWindow", u"Color (Green):", None))
        self.blue_label.setText(QCoreApplication.translate("MainWindow", u"Color (Blue):", None))
        self.agregarinicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar part\u00edcula al inicio", None))
        self.agregarfinal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar part\u00edcula al final", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar part\u00edculas", None))
    # retranslateUi

