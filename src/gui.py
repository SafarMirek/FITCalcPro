# Graficke uzivatelske rozhrani

# Autor: Matěj Mudra
# Datum: 4.3.2021

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from guiMainWindow import Ui_mainWindow

##
# @brief Inicializuje rozložení aplikace
#
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

    ##
    # @brief Namapuje funkce na příslušné klávesy
    #
    def keyPressEvent(self, event):
        if event.text() == "0":
            self.ui.number_button_press(u"0", False)
        elif event.text() == "1":
            self.ui.number_button_press(u"1", False)
        elif event.text() == "2":
            self.ui.number_button_press(u"2", False)
        elif event.text() == "3":
            self.ui.number_button_press(u"3", False)
        elif event.text() == "4":
            self.ui.number_button_press(u"4", False)
        elif event.text() == "5":
            self.ui.number_button_press(u"5", False)
        elif event.text() == "6":
            self.ui.number_button_press(u"6", False)
        elif event.text() == "7":
            self.ui.number_button_press(u"7", False)
        elif event.text() == "8":
            self.ui.number_button_press(u"8", False)
        elif event.text() == "9":
            self.ui.number_button_press(u"9", False)
        elif event.text() == "," or event.text() == ".":
            self.ui.number_button_press(u",", False)
        elif event.text() == "+":
            self.ui.function_button_press(self.ui.a_label, "plus")
        elif event.text() == "-":
            self.ui.function_button_press(self.ui.a_label, "minus")
        elif event.text() == "*":
            self.ui.function_button_press(self.ui.a_label, "times")
        elif event.text() == "/":
            self.ui.function_button_press(self.ui.a_label, "devide")
        elif event.key() == 16777219:
            self.ui.delete_char(False)
        elif event.key() == 16777220 or event.key() == 16777221:
            self.ui.function_button_press(self.ui.a_label, "equals")
        elif event.text() == "s":
            self.ui.function_button_press(self.ui.a_label, "sin")
        elif event.text() == "c":
            self.ui.function_button_press(self.ui.a_label, "cos")
        elif event.text() == "t":
            self.ui.function_button_press(self.ui.a_label, "tan")
        elif event.text() == "i":
            self.ui.function_button_press(self.ui.a_label, "invert")
        elif event.text() == "f":
            self.ui.function_button_press(self.ui.a_label, "factorial")
        elif event.key() == 16777223:
            self.ui.clear_all()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

