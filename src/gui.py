# Graficke uzivatelske rozhrani

# Autor: Matěj Mudra
# Datum: 4.3.2021

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from guiMainWindow import Ui_mainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

