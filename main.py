import sys
from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow

# Aplicación de Qt
app = QApplication()

# Crear y mostrar nuestra ventana principal
window = MainWindow()
window.show()

# Qt loop
sys.exit(app.exec_())