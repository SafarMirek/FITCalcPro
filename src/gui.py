# Graficke uzivatelske rozhrani

# Autor: Matěj Mudra
# Datum: 4.3.2021

import sys

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox

from guiMainWindow import Ui_mainWindow


##
# @brief Třída hlavního okna
#
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("FITCalcProIcon.png"))

    ##
    # @brief Namapuje funkce na příslušné klávesy
    # param event Tlačítko, které je voláno
    #
    def keyPressEvent(self, event):
        if event.text() == "0":
            self.ui.number_button_press(u"0")
        elif event.text() == "1":
            self.ui.number_button_press(u"1")
        elif event.text() == "2":
            self.ui.number_button_press(u"2")
        elif event.text() == "3":
            self.ui.number_button_press(u"3")
        elif event.text() == "4":
            self.ui.number_button_press(u"4")
        elif event.text() == "5":
            self.ui.number_button_press(u"5")
        elif event.text() == "6":
            self.ui.number_button_press(u"6")
        elif event.text() == "7":
            self.ui.number_button_press(u"7")
        elif event.text() == "8":
            self.ui.number_button_press(u"8")
        elif event.text() == "9":
            self.ui.number_button_press(u"9")
        elif event.text() == "," or event.text() == ".":
            self.ui.number_button_press(u",")
        elif event.text() == "+":
            self.ui.function_button_press(self.ui.input, "plus")
        elif event.text() == "-":
            self.ui.decide_minus()
        elif event.text() == "*":
            self.ui.function_button_press(self.ui.input, "times")
        elif event.text() == "/":
            self.ui.function_button_press(self.ui.input, "devide")
        elif event.key() == 16777219:
            self.ui.delete_char()
        elif event.key() == 16777220 or event.key() == 16777221:
            self.ui.function_button_press(self.ui.input, "equals")
        elif event.text() == "s":
            self.ui.function_button_press(self.ui.input, "sin")
        elif event.text() == "c":
            self.ui.function_button_press(self.ui.input, "cos")
        elif event.text() == "t":
            self.ui.function_button_press(self.ui.input, "tan")
        elif event.text() == "i":
            self.ui.function_button_press(self.ui.input, "invert")
        elif event.text() == "f":
            self.ui.function_button_press(self.ui.input, "factorial")
        elif event.key() == 16777223:
            self.ui.clear_all()

    ##
    # @brief Vypíše chybu v separátním podokně a ukončí aplikaci
    #
    def show_error_window(self):
        self.error = QMessageBox()
        self.error.setWindowTitle("Chyba")
        self.error.setInformativeText("Omlouváme se, něco se nepovedlo.")
        self.error.setIcon(QMessageBox.Warning)
        self.error.setStandardButtons(QMessageBox.Ok)
        err_msg = self.error.exec_()
        app.exit(1)


##
# @brief Zachytí chybu a zobrazí chybové okno
# @param exctype Typ chyby
# @param value Hodnota chyby
# @param traceback Shrnutí chyby
#
def error_hook(exctype, value, traceback):
    MainWindow.show_error_window(window)
    run()


##
# @brief Spustí kalkulačku
#
def run():
    window.show()
    exit(app.exec_())


sys.excepthook = error_hook
app = QApplication(sys.argv)
window = MainWindow()

run()
