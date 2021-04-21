##
# @file guiMainWindow.py
# @brief Hlavní okno s metodami pro vizualizaci uživatelských akcí
# @author Matěj Mudra <xmudra04.stud.fit.vutbr.cz>
#
# * Project: fit-ivs-2
# * Date created: 2021-03-04
# * Last modified: 20201-03-21
#

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiDesign.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
################################################################################
import os
import sys
import webbrowser

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ButtonActions import *
from math_interpreter import *
from math_lib import *

regular_pi = "\u03c0"


##
# @brief Třída s rozložením kalkulačky
#
class Ui_mainWindow(object):
    def __init__(self):
        self.ans = 0
        self.input = ""
        self.output = [ ]
        self.members = [ ]
        self.operations = [ ]
        self.calc_done = False
        self.error_raised = False
        self.num_is_ready = False
        self.operation_needed = False
        self.doc_path = f"{os.path.dirname(sys.argv[0])}/TODO" # TODO
        self.guide_path = f"{os.path.dirname(sys.argv[0])}/TODO" # TODO

        self.buttonActions = [
            ButtonAction("sin", "sin({value})", lambda a: sin(a), True),
            ButtonAction("cos", "cos({value})", lambda a: cos(a), True),
            ButtonAction("tan", "tan({value})", lambda a: tan(a), True),
            ButtonAction("factorial", "{value}!", lambda a: factorial(a), True),
            ButtonAction("plus", "+", "+", False),
            ButtonAction("minus", "-", "-", False),
            ButtonAction("times", "\u00B7", "*", False),
            ButtonAction("devide", "/", "/", False),
            ButtonAction("twopowerx", "{value}" + f"{self.convert_to_superscript(2)}", lambda a: power(a, 2), True),
            ButtonAction("tworootx", f"{self.convert_to_superscript(2)}\u221a" + "{value}", lambda a: nth_root(a, 2),
                         True),
            ButtonAction("invert", "{value}", lambda a: a * (-1), True),
            CustomButtonAction("xpowery", "^\u25a1", "power", lambda a, b: a + self.string_to_superscript(b)),
            CustomButtonAction("yrootx", "\u221a\u25a1", "root",
                               lambda a, b: self.string_to_superscript(a) + "\u221a" + b),
            PiButtonAction("pi", "{value}\u03c0", lambda a: a * pi, True, 1),
            PiButtonAction("ans", "Ans", lambda a: a * self.ans, True, 1),
        ]

    ##
    # @brief Přeformátuje posledního člena
    #
    def format_last_member(self, output):
        if isinstance(output[ -1 ], ButtonAction):
            return output[ -1 ].get_formatted(self.format_last_member(output[ :-1 ]))
        return output[ -1 ]

    ##
    # @brief Při zadájní vstupu aktualizuje obsah sekce výstupů
    #
    def update_input(self):
        if self.input == "":
            if len(self.output) >= 2:
                if isinstance(self.output[ -1 ], ButtonAction) and self.output[ -1 ].instant:
                    self.action_label.setText(
                        QCoreApplication.translate("mainWindow", self.format_last_member(self.output), None))
                return
        self.action_label.setText(QCoreApplication.translate("mainWindow", self.input, None))

    ##
    # @brief Přidá číslo do skece vstupů
    # @param input Text, který bude přidán do sekce vstupů
    #
    def set_input(self, input):
        self.input = str(input)
        self.update_input()

    ##
    # @brief Vymaže sekci vstupů
    #
    def clear_input(self):
        self.set_input("")

    ##
    # @brief Přidá číslo do skece vstupů
    # @param to_add Text, který bude přidán do sekce vstupů
    #
    def add_to_input(self, to_add):
        if self.operation_needed:
            return

        if len(self.input) > 22:
            return

        self.input += f"{to_add}"
        self.num_is_ready = to_add != "," and to_add != "-"
        self.action_label.setText(
            QCoreApplication.translate("mainWindow", self.input, None))

    ##
    # @brief Přidá číslo do zásobníku vstupů
    # @param to_add Text, který bude přidán do zásobníku výtupů
    #
    def add_to_output_buffer(self, to_add):
        self.output.append(to_add)
        self.reformat_output()
        if not self.calc_done:
            self.clear_input()

    ##
    # @brief Převede uživatelské vstupy na požadovaný formát pro výpis
    #
    def reformat_output(self):
        output = self.output.copy()
        output_str = ""
        i = 0
        while i < len(output):
            if isinstance(output[ i ], ButtonAction):
                if output[ i ].instant:
                    output[ i - 1 ] = output[ i ].get_formatted(output[ i - 1 ])
                    del output[ i ]
                    continue
            i = i + 1
        i = 0
        while i < len(output) - 1:
            if isinstance(output[ i ], CustomButtonAction):
                output[ i - 1 ] = output[ i ].to_superscript_fce(str(output[ i - 1 ]), str(output[ i + 1 ]))
                del output[ i + 1 ]
                del output[ i ]
                continue
            i = i + 1

        for member in output:
            output_str += str(member) + " "
        self.buffer_label.setText(QCoreApplication.translate("mainWindow", output_str, None))

    ##
    # @brief Převádí zadaný text na horní index
    # @param char Charakter, který bude převeden na horní index
    #
    def convert_to_superscript(self, char):
        char = str(char)
        sup_chars = {
            "0": u'\u2070',
            "1": u'\u00B9',
            "2": u'\u00B2',
            "3": u'\u00B3',
            "4": u'\u2074',
            "5": u'\u2075',
            "6": u'\u2076',
            "7": u'\u2077',
            "8": u'\u2078',
            "9": u'\u2079',
            u"\u03c0": u"\u2DEB",
            "-": u"\u207B",
            "t": u"\u1D57",
            "o": u"\u1D52",
            "a": u"\u1D43",
            "c": u"\u1D9C",
            "n": u"\u207F",
            "i": u"\u2071",
            "s": u"\u02E2",
            "(": u"\u207d",
            ")": u"\u207e",
            ",": u"\u22C5",
        }
        return sup_chars.get(char, ' ')

    ##
    # @brief Převede libovolně dlouhý string na horní index
    # @param string Text, který bude převeden na horní index
    #
    def string_to_superscript(self, string):
        output = ""
        for char in string:
            output += f"{self.convert_to_superscript(char)}"
        return output

    ##
    # @brief Funkce vyvolaná stisknutím tlačítka
    # @param button_text Text, který bude předán do inputu
    #
    def number_button_press(self, button_text):
        if self.calc_done:  # Vyresetuje kalkulačku, když po = začneme zadávat čísla
            self.clear_all()
            self.calc_done = False

        if button_text == "," and "," in self.input:
            return
        elif self.input == "" and button_text == ",":
            return

        self.add_to_input(button_text)

    ##
    # @brief Vyčistí a resetuje o všechny parametry kalkulačky do startovací hodnoty
    #
    def clear_all(self):
        self.calc_done = False
        self.error_raised = False
        self.num_is_ready = False
        self.operation_needed = False

        self.output = [ ]
        self.operations = [ ]
        self.members = [ ]
        self.clear_input()
        self.reformat_output()

    ##
    # @brief Resetuje kalkulačku pokud nastane chyba
    #
    def exit_on_error(self):
        self.clear_all()
        self.action_label.setText(
            QCoreApplication.translate("mainWindow", "Math error", None))

    ##
    # @brief Funkce vyvolaná stisknutím tlačítka
    # @param text String na jehož vstupu se funkce provede
    # @param button Tlačítko jehož funkce se provede
    #
    def function_button_press(self, text, button):
        if self.calc_done:  # Pokračování ve výpočtech po = (použití answer)
            self.clear_all()
            self.calc_done = False
            self.num_is_ready = True

        if self.error_raised:
            self.input = self.input[ 1: ]
            self.error_raised = False

        if button == "equals":
            self.calc_and_print(text)
            return

        for buttonAction in self.buttonActions:
            if buttonAction.name == button:
                self.process_action(text, buttonAction)
                break

        self.operation_needed = len(self.members) == len(self.operations) + 1

    ##
    # @brief Zpracuje zadanou funkci
    # @param text Text z uživatelského vstupu
    # @param button_action Aḱce, která se má zpracovat
    #
    def process_action(self, text, button_action):
        try:
            if self.operation_needed:
                self.make_append(button_action, text)
                self.add_to_output_buffer(button_action)
                return
            if not self.num_is_ready:
                if not button_action.has_implicit_value() or text != "":
                    return
                text = str(button_action.implicit_value)
            self.append_type(text)

            text = self.make_append(button_action, text)
            self.add_to_output_buffer(text)
            self.add_to_output_buffer(button_action)

            self.num_is_ready = False
        except ValueError:
            self.exit_on_error()

    ##
    # @brief Vloží operaci a číslo na zásobník, provede instantní funkce
    # @param action Akce, která se má provést
    # @param text Text, který se podle potřeby upraví
    # @return Vrací upravený text
    #
    def make_append(self, action, text):
        if action.instant:
            x = self.members.pop()
            self.members.append(action.operation(x))
            if action.name == "invert":
                return str(self.members[ -1 ])
            return text
        self.operations.append(action.operation)
        return text

    ##
    # @brief Odstraní charakter, nebo celou sekci vstupů
    #
    def delete_char(self):
        if self.calc_done:
            self.clear_all()
        else:
            self.input = self.input[ :-1 ]
            self.action_label.setText(QCoreApplication.translate("mainWindow", self.input, None))

    ##
    # @brief Přidá do zásobníku zbylou hodnotu, vypočítá obsah kalkulačky a vytiskne na výstup číslo dle jeho typu
    # @param text Hodnota z pole vstupů
    #
    def calc_and_print(self, text):
        if text != "":
            self.append_type(text)
            self.add_to_output_buffer(text)
        try:
            self.ans = eval(self.members, self.operations)
        except (ValueError, IndexError):
            self.exit_on_error()
            return
        self.num_is_ready = False
        self.operation_needed = False
        self.clear_all()

        if isinstance(self.ans, float):
            if f"{self.ans}".rpartition('.')[ 2 ] == "0":
                self.ans = int(self.ans)
            else:
                self.ans = round(float(self.ans), accuracy)

        while len(str(self.ans)) > 22:
            if isinstance(self.ans, int):
                try:
                    self.ans = float(self.ans)
                    continue
                except:
                    pass
            self.exit_on_error()
            return
        self.set_input(f"{self.ans}".replace(".", ","))

        self.calc_done = True

    ##
    # @brief Přidá do zásobníku členů číslo ve správném typu
    # @param input_number Číslo, které bude přidáno
    #
    def append_type(self, input_number):
        if "," in input_number or "." in input_number:
            self.members.append(float(input_number.replace(",", ".")))
        elif regular_pi in input_number:
            self.members.append(float(pi))
        else:
            self.members.append(int(input_number))

    ##
    # @brief Rozhodne zda se mínus bude chovat jako znaménko, nebo operace
    #
    def decide_minus(self):
        if self.input == "":
            self.number_button_press(u"-")
        else:
            self.function_button_press(self.input, "minus")

    ##
    # @brief Inicializuje rozložení aplikace
    #
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(400, 600)
        mainWindow.setFixedSize(QSize(400, 600))
        mainWindow.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 120, 401, 451))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.xpowery = QPushButton(self.layoutWidget)
        self.xpowery.setObjectName(u"xpowery")
        self.xpowery.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xpowery.sizePolicy().hasHeightForWidth())
        self.xpowery.setSizePolicy(sizePolicy)
        self.xpowery.setMaximumSize(QSize(60, 60))
        font = QFont()
        font.setPointSize(20)
        self.xpowery.setFont(font)
        self.xpowery.setAutoFillBackground(False)
        self.xpowery.setStyleSheet(u"QPushButton {\n"
                                   "	border: 1px;\n"
                                   "	background-color: rgb(20,20,20);\n"
                                   "	color: rgb(255, 255, 255);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "	background-color: rgb(30,30,30);\n"
                                   "	color: rgb(255, 255, 255);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed {\n"
                                   "	background-color: rgb(200,200,200);\n"
                                   "	color: rgb(30, 30, 30);\n"
                                   "}")
        self.xpowery.setFlat(True)
        self.xpowery.clicked.connect(lambda: self.function_button_press(self.input, "xpowery"))

        self.gridLayout.addWidget(self.xpowery, 0, 0, 1, 1)

        self.yrootx = QPushButton(self.layoutWidget)
        self.yrootx.setObjectName(u"yrootx")
        self.yrootx.setEnabled(True)
        sizePolicy.setHeightForWidth(self.yrootx.sizePolicy().hasHeightForWidth())
        self.yrootx.setSizePolicy(sizePolicy)
        self.yrootx.setMaximumSize(QSize(60, 60))
        self.yrootx.setFont(font)
        self.yrootx.setAutoFillBackground(False)
        self.yrootx.setStyleSheet(u"QPushButton {\n"
                                  "	border: 1px;\n"
                                  "	background-color: rgb(20,20,20);\n"
                                  "	color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover {\n"
                                  "	background-color: rgb(30,30,30);\n"
                                  "	color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:pressed {\n"
                                  "	background-color: rgb(200,200,200);\n"
                                  "	color: rgb(30, 30, 30);\n"
                                  "}")
        self.yrootx.setFlat(True)
        self.yrootx.clicked.connect(lambda: self.function_button_press(self.input, "yrootx"))

        self.gridLayout.addWidget(self.yrootx, 0, 1, 1, 1)

        self.twopowerx = QPushButton(self.layoutWidget)
        self.twopowerx.setObjectName(u"twopowerx")
        self.twopowerx.setEnabled(True)
        sizePolicy.setHeightForWidth(self.twopowerx.sizePolicy().hasHeightForWidth())
        self.twopowerx.setSizePolicy(sizePolicy)
        self.twopowerx.setMaximumSize(QSize(60, 60))
        self.twopowerx.setFont(font)
        self.twopowerx.setAutoFillBackground(False)
        self.twopowerx.setStyleSheet(u"QPushButton {\n"
                                     "	border: 1px;\n"
                                     "	background-color: rgb(20,20,20);\n"
                                     "	color: rgb(255, 255, 255);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "	background-color: rgb(30,30,30);\n"
                                     "	color: rgb(255, 255, 255);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "	background-color: rgb(200,200,200);\n"
                                     "	color: rgb(30, 30, 30);\n"
                                     "}")
        self.twopowerx.setFlat(True)
        self.twopowerx.clicked.connect(lambda: self.function_button_press(self.input, "twopowerx"))

        self.gridLayout.addWidget(self.twopowerx, 0, 2, 1, 1)

        self.tworootx = QPushButton(self.layoutWidget)
        self.tworootx.setObjectName(u"tworootx")
        self.tworootx.setEnabled(True)
        sizePolicy.setHeightForWidth(self.tworootx.sizePolicy().hasHeightForWidth())
        self.tworootx.setSizePolicy(sizePolicy)
        self.tworootx.setMaximumSize(QSize(60, 60))
        self.tworootx.setFont(font)
        self.tworootx.setAutoFillBackground(False)
        self.tworootx.setStyleSheet(u"QPushButton {\n"
                                    "	border: 1px;\n"
                                    "	background-color: rgb(20,20,20);\n"
                                    "	color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "	background-color: rgb(30,30,30);\n"
                                    "	color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "	background-color: rgb(200,200,200);\n"
                                    "	color: rgb(30, 30, 30);\n"
                                    "}")
        self.tworootx.setFlat(True)
        self.tworootx.clicked.connect(lambda: self.function_button_press(self.input, "tworootx"))

        self.gridLayout.addWidget(self.tworootx, 0, 3, 1, 1)

        self.factorial = QPushButton(self.layoutWidget)
        self.factorial.setObjectName(u"factorial")
        self.factorial.setEnabled(True)
        sizePolicy.setHeightForWidth(self.factorial.sizePolicy().hasHeightForWidth())
        self.factorial.setSizePolicy(sizePolicy)
        self.factorial.setMaximumSize(QSize(60, 60))
        self.factorial.setFont(font)
        self.factorial.setAutoFillBackground(False)
        self.factorial.setStyleSheet(u"QPushButton {\n"
                                     "	border: 1px;\n"
                                     "	background-color: rgb(20,20,20);\n"
                                     "	color: rgb(255, 255, 255);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "	background-color: rgb(30,30,30);\n"
                                     "	color: rgb(255, 255, 255);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "	background-color: rgb(200,200,200);\n"
                                     "	color: rgb(30, 30, 30);\n"
                                     "}")
        self.factorial.setFlat(True)
        self.factorial.clicked.connect(lambda: self.function_button_press(self.input, "factorial"))

        self.gridLayout.addWidget(self.factorial, 0, 4, 1, 1)

        self.invertor = QPushButton(self.layoutWidget)
        self.invertor.setObjectName(u"invertor")
        self.invertor.setEnabled(True)
        sizePolicy.setHeightForWidth(self.invertor.sizePolicy().hasHeightForWidth())
        self.invertor.setSizePolicy(sizePolicy)
        self.invertor.setMaximumSize(QSize(60, 60))
        self.invertor.setFont(font)
        self.invertor.setAutoFillBackground(False)
        self.invertor.setStyleSheet(u"QPushButton {\n"
                                    "	border: 1px;\n"
                                    "	background-color: rgb(20,20,20);\n"
                                    "	color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "	background-color: rgb(30,30,30);\n"
                                    "	color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "	background-color: rgb(200,200,200);\n"
                                    "	color: rgb(30, 30, 30);\n"
                                    "}")
        self.invertor.setFlat(True)
        self.invertor.clicked.connect(lambda: self.function_button_press(self.input, "invert"))

        self.gridLayout.addWidget(self.invertor, 1, 0, 1, 1)

        self.sin = QPushButton(self.layoutWidget)
        self.sin.setObjectName(u"sin")
        self.sin.setEnabled(True)
        sizePolicy.setHeightForWidth(self.sin.sizePolicy().hasHeightForWidth())
        self.sin.setSizePolicy(sizePolicy)
        self.sin.setMaximumSize(QSize(60, 60))
        self.sin.setFont(font)
        self.sin.setAutoFillBackground(False)
        self.sin.setStyleSheet(u"QPushButton {\n"
                               "	border: 1px;\n"
                               "	background-color: rgb(20,20,20);\n"
                               "	color: rgb(255, 255, 255);\n"
                               "}\n"
                               "\n"
                               "QPushButton:hover {\n"
                               "	background-color: rgb(30,30,30);\n"
                               "	color: rgb(255, 255, 255);\n"
                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "	background-color: rgb(200,200,200);\n"
                               "	color: rgb(30, 30, 30);\n"
                               "}")
        self.sin.setFlat(True)
        self.sin.clicked.connect(lambda: self.function_button_press(self.input, "sin"))

        self.gridLayout.addWidget(self.sin, 1, 1, 1, 1)

        self.cos = QPushButton(self.layoutWidget)
        self.cos.setObjectName(u"cos")
        self.cos.setEnabled(True)
        sizePolicy.setHeightForWidth(self.cos.sizePolicy().hasHeightForWidth())
        self.cos.setSizePolicy(sizePolicy)
        self.cos.setMaximumSize(QSize(60, 60))
        self.cos.setFont(font)
        self.cos.setAutoFillBackground(False)
        self.cos.setStyleSheet(u"QPushButton {\n"
                               "	border: 1px;\n"
                               "	background-color: rgb(20,20,20);\n"
                               "	color: rgb(255, 255, 255);\n"
                               "}\n"
                               "\n"
                               "QPushButton:hover {\n"
                               "	background-color: rgb(30,30,30);\n"
                               "	color: rgb(255, 255, 255);\n"
                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "	background-color: rgb(200,200,200);\n"
                               "	color: rgb(30, 30, 30);\n"
                               "}")
        self.cos.setFlat(True)
        self.cos.clicked.connect(lambda: self.function_button_press(self.input, "cos"))

        self.gridLayout.addWidget(self.cos, 1, 2, 1, 1)

        self.tan = QPushButton(self.layoutWidget)
        self.tan.setObjectName(u"tan")
        self.tan.setEnabled(True)
        sizePolicy.setHeightForWidth(self.tan.sizePolicy().hasHeightForWidth())
        self.tan.setSizePolicy(sizePolicy)
        self.tan.setMaximumSize(QSize(60, 60))
        self.tan.setFont(font)
        self.tan.setAutoFillBackground(False)
        self.tan.setStyleSheet(u"QPushButton {\n"
                               "	border: 1px;\n"
                               "	background-color: rgb(20,20,20);\n"
                               "	color: rgb(255, 255, 255);\n"
                               "}\n"
                               "\n"
                               "QPushButton:hover {\n"
                               "	background-color: rgb(30,30,30);\n"
                               "	color: rgb(255, 255, 255);\n"
                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "	background-color: rgb(200,200,200);\n"
                               "	color: rgb(30, 30, 30);\n"
                               "}")
        self.tan.setFlat(True)
        self.tan.clicked.connect(lambda: self.function_button_press(self.input, "tan"))

        self.gridLayout.addWidget(self.tan, 1, 3, 1, 1)

        self.pi = QPushButton(self.layoutWidget)
        self.pi.setObjectName(u"pi")
        self.pi.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pi.sizePolicy().hasHeightForWidth())
        self.pi.setSizePolicy(sizePolicy)
        self.pi.setMaximumSize(QSize(60, 60))
        self.pi.setFont(font)
        self.pi.setAutoFillBackground(False)
        self.pi.setStyleSheet(u"QPushButton {\n"
                              "	border: 1px;\n"
                              "	background-color: rgb(20,20,20);\n"
                              "	color: rgb(255, 255, 255);\n"
                              "}\n"
                              "\n"
                              "QPushButton:hover {\n"
                              "	background-color: rgb(30,30,30);\n"
                              "	color: rgb(255, 255, 255);\n"
                              "}\n"
                              "\n"
                              "QPushButton:pressed {\n"
                              "	background-color: rgb(200,200,200);\n"
                              "	color: rgb(30, 30, 30);\n"
                              "}")
        self.pi.setFlat(True)
        self.pi.clicked.connect(lambda: self.function_button_press(self.input, "pi"))

        self.gridLayout.addWidget(self.pi, 1, 4, 1, 1)

        self.seven = QPushButton(self.layoutWidget)
        self.seven.setObjectName(u"seven")
        self.seven.setEnabled(True)
        sizePolicy.setHeightForWidth(self.seven.sizePolicy().hasHeightForWidth())
        self.seven.setSizePolicy(sizePolicy)
        self.seven.setMaximumSize(QSize(60, 60))
        self.seven.setFont(font)
        self.seven.setAutoFillBackground(False)
        self.seven.setStyleSheet(u"QPushButton {\n"
                                 "	border: 1px;\n"
                                 "	background-color: rgb(20,20,20);\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "	background-color: rgb(30,30,30);\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "	background-color: rgb(200,200,200);\n"
                                 "	color: rgb(30, 30, 30);\n"
                                 "}")
        self.seven.setFlat(True)
        self.seven.clicked.connect(lambda: self.number_button_press(u"7"))

        self.gridLayout.addWidget(self.seven, 2, 0, 1, 1)

        self.eight = QPushButton(self.layoutWidget)
        self.eight.setObjectName(u"eight")
        self.eight.setEnabled(True)
        sizePolicy.setHeightForWidth(self.eight.sizePolicy().hasHeightForWidth())
        self.eight.setSizePolicy(sizePolicy)
        self.eight.setMaximumSize(QSize(60, 60))
        self.eight.setFont(font)
        self.eight.setAutoFillBackground(False)
        self.eight.setStyleSheet(u"QPushButton {\n"
                                 "	border: 1px;\n"
                                 "	background-color: rgb(20,20,20);\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "	background-color: rgb(30,30,30);\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "	background-color: rgb(200,200,200);\n"
                                 "	color: rgb(30, 30, 30);\n"
                                 "}")
        self.eight.setFlat(True)
        self.eight.clicked.connect(lambda: self.number_button_press(u"8"))

        self.gridLayout.addWidget(self.eight, 2, 1, 1, 1)

        self.nine = QPushButton(self.layoutWidget)
        self.nine.setObjectName(u"nine")
        self.nine.setEnabled(True)
        sizePolicy.setHeightForWidth(self.nine.sizePolicy().hasHeightForWidth())
        self.nine.setSizePolicy(sizePolicy)
        self.nine.setMaximumSize(QSize(60, 60))
        self.nine.setFont(font)
        self.nine.setAutoFillBackground(False)
        self.nine.setStyleSheet(u"QPushButton {\n"
                                "	border: 1px;\n"
                                "	background-color: rgb(20,20,20);\n"
                                "	color: rgb(255, 255, 255);\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "	background-color: rgb(30,30,30);\n"
                                "	color: rgb(255, 255, 255);\n"
                                "}\n"
                                "\n"
                                "QPushButton:pressed {\n"
                                "	background-color: rgb(200,200,200);\n"
                                "	color: rgb(30, 30, 30);\n"
                                "}")
        self.nine.setFlat(True)
        self.nine.clicked.connect(lambda: self.number_button_press(u"9"))

        self.gridLayout.addWidget(self.nine, 2, 2, 1, 1)

        self.ac = QPushButton(self.layoutWidget)
        self.ac.setObjectName(u"ac")
        self.ac.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ac.sizePolicy().hasHeightForWidth())
        self.ac.setSizePolicy(sizePolicy)
        self.ac.setMaximumSize(QSize(60, 60))
        self.ac.setFont(font)
        self.ac.setAutoFillBackground(False)
        self.ac.setStyleSheet(u"QPushButton {\n"
                              "	border: 1px;\n"
                              "	background-color: rgb(20,20,20);\n"
                              "	color: rgb(255, 255, 255);\n"
                              "}\n"
                              "\n"
                              "QPushButton:hover {\n"
                              "	background-color: rgb(30,30,30);\n"
                              "	color: rgb(255, 255, 255);\n"
                              "}\n"
                              "\n"
                              "QPushButton:pressed {\n"
                              "	background-color: rgb(200,200,200);\n"
                              "	color: rgb(30, 30, 30);\n"
                              "}")
        self.ac.setFlat(True)
        self.ac.clicked.connect(lambda: self.clear_all())

        self.gridLayout.addWidget(self.ac, 2, 3, 1, 1)

        self.delete = QPushButton(self.layoutWidget)
        self.delete.setObjectName(u"del")
        self.delete.setEnabled(True)
        sizePolicy.setHeightForWidth(self.delete.sizePolicy().hasHeightForWidth())
        self.delete.setSizePolicy(sizePolicy)
        self.delete.setMaximumSize(QSize(60, 60))
        self.delete.setFont(font)
        self.delete.setAutoFillBackground(False)
        self.delete.setStyleSheet(u"QPushButton {\n"
                                  "	border: 1px;\n"
                                  "	background-color: rgb(20,20,20);\n"
                                  "	color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover {\n"
                                  "	background-color: rgb(30,30,30);\n"
                                  "	color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:pressed {\n"
                                  "	background-color: rgb(200,200,200);\n"
                                  "	color: rgb(30, 30, 30);\n"
                                  "}")
        self.delete.setFlat(True)
        self.delete.clicked.connect(lambda: self.delete_char())

        self.gridLayout.addWidget(self.delete, 2, 4, 1, 1)

        self.four = QPushButton(self.layoutWidget)
        self.four.setObjectName(u"four")
        self.four.setEnabled(True)
        sizePolicy.setHeightForWidth(self.four.sizePolicy().hasHeightForWidth())
        self.four.setSizePolicy(sizePolicy)
        self.four.setMaximumSize(QSize(60, 60))
        self.four.setFont(font)
        self.four.setAutoFillBackground(False)
        self.four.setStyleSheet(u"QPushButton {\n"
                                "	border: 1px;\n"
                                "	background-color: rgb(20,20,20);\n"
                                "	color: rgb(255, 255, 255);\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "	background-color: rgb(30,30,30);\n"
                                "	color: rgb(255, 255, 255);\n"
                                "}\n"
                                "\n"
                                "QPushButton:pressed {\n"
                                "	background-color: rgb(200,200,200);\n"
                                "	color: rgb(30, 30, 30);\n"
                                "}")
        self.four.setFlat(True)
        self.four.clicked.connect(lambda: self.number_button_press(u"4"))

        self.gridLayout.addWidget(self.four, 3, 0, 1, 1)

        self.five = QPushButton(self.layoutWidget)
        self.five.setObjectName(u"five")
        self.five.setEnabled(True)
        sizePolicy.setHeightForWidth(self.five.sizePolicy().hasHeightForWidth())
        self.five.setSizePolicy(sizePolicy)
        self.five.setMaximumSize(QSize(60, 60))
        self.five.setFont(font)
        self.five.setAutoFillBackground(False)
        self.five.setStyleSheet(u"QPushButton {\n"
                                "	border: 1px;\n"
                                "	background-color: rgb(20,20,20);\n"
                                "	color: rgb(255, 255, 255);\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "	background-color: rgb(30,30,30);\n"
                                "	color: rgb(255, 255, 255);\n"
                                "}\n"
                                "\n"
                                "QPushButton:pressed {\n"
                                "	background-color: rgb(200,200,200);\n"
                                "	color: rgb(30, 30, 30);\n"
                                "}")
        self.five.setFlat(True)
        self.five.clicked.connect(lambda: self.number_button_press(u"5"))

        self.gridLayout.addWidget(self.five, 3, 1, 1, 1)

        self.six = QPushButton(self.layoutWidget)
        self.six.setObjectName(u"six")
        self.six.setEnabled(True)
        sizePolicy.setHeightForWidth(self.six.sizePolicy().hasHeightForWidth())
        self.six.setSizePolicy(sizePolicy)
        self.six.setMaximumSize(QSize(60, 60))
        self.six.setFont(font)
        self.six.setAutoFillBackground(False)
        self.six.setStyleSheet(u"QPushButton {\n"
                               "	border: 1px;\n"
                               "	background-color: rgb(20,20,20);\n"
                               "	color: rgb(255, 255, 255);\n"
                               "}\n"
                               "\n"
                               "QPushButton:hover {\n"
                               "	background-color: rgb(30,30,30);\n"
                               "	color: rgb(255, 255, 255);\n"
                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "	background-color: rgb(200,200,200);\n"
                               "	color: rgb(30, 30, 30);\n"
                               "}")
        self.six.setFlat(True)
        self.six.clicked.connect(lambda: self.number_button_press(u"6"))

        self.gridLayout.addWidget(self.six, 3, 2, 1, 1)

        self.times = QPushButton(self.layoutWidget)
        self.times.setObjectName(u"times")
        self.times.setEnabled(True)
        sizePolicy.setHeightForWidth(self.times.sizePolicy().hasHeightForWidth())
        self.times.setSizePolicy(sizePolicy)
        self.times.setMaximumSize(QSize(60, 60))
        self.times.setFont(font)
        self.times.setAutoFillBackground(False)
        self.times.setStyleSheet(u"QPushButton {\n"
                                 "	border: 1px;\n"
                                 "	background-color: rgb(20,20,20);\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "	background-color: rgb(30,30,30);\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "	background-color: rgb(200,200,200);\n"
                                 "	color: rgb(30, 30, 30);\n"
                                 "}")
        self.times.setFlat(True)
        self.times.clicked.connect(lambda: self.function_button_press(self.input, "times"))

        self.gridLayout.addWidget(self.times, 3, 3, 1, 1)

        self.devide = QPushButton(self.layoutWidget)
        self.devide.setObjectName(u"devide")
        self.devide.setEnabled(True)
        sizePolicy.setHeightForWidth(self.devide.sizePolicy().hasHeightForWidth())
        self.devide.setSizePolicy(sizePolicy)
        self.devide.setMaximumSize(QSize(60, 60))
        self.devide.setFont(font)
        self.devide.setAutoFillBackground(False)
        self.devide.setStyleSheet(u"QPushButton {\n"
                                  "	border: 1px;\n"
                                  "	background-color: rgb(20,20,20);\n"
                                  "	color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover {\n"
                                  "	background-color: rgb(30,30,30);\n"
                                  "	color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:pressed {\n"
                                  "	background-color: rgb(200,200,200);\n"
                                  "	color: rgb(30, 30, 30);\n"
                                  "}")
        self.devide.setFlat(True)
        self.devide.clicked.connect(lambda: self.function_button_press(self.input, "devide"))

        self.gridLayout.addWidget(self.devide, 3, 4, 1, 1)

        self.one = QPushButton(self.layoutWidget)
        self.one.setObjectName(u"one")
        self.one.setEnabled(True)
        sizePolicy.setHeightForWidth(self.one.sizePolicy().hasHeightForWidth())
        self.one.setSizePolicy(sizePolicy)
        self.one.setMaximumSize(QSize(60, 60))
        self.one.setFont(font)
        self.one.setAutoFillBackground(False)
        self.one.setStyleSheet(u"QPushButton {\n"
                               "	border: 1px;\n"
                               "	background-color: rgb(20,20,20);\n"
                               "	color: rgb(255, 255, 255);\n"
                               "}\n"
                               "\n"
                               "QPushButton:hover {\n"
                               "	background-color: rgb(30,30,30);\n"
                               "	color: rgb(255, 255, 255);\n"
                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "	background-color: rgb(200,200,200);\n"
                               "	color: rgb(30, 30, 30);\n"
                               "}")
        self.one.setFlat(True)
        self.one.clicked.connect(lambda: self.number_button_press(u"1"))

        self.gridLayout.addWidget(self.one, 4, 0, 1, 1)

        self.two = QPushButton(self.layoutWidget)
        self.two.setObjectName(u"two")
        self.two.setEnabled(True)
        sizePolicy.setHeightForWidth(self.two.sizePolicy().hasHeightForWidth())
        self.two.setSizePolicy(sizePolicy)
        self.two.setMaximumSize(QSize(60, 60))
        self.two.setFont(font)
        self.two.setAutoFillBackground(False)
        self.two.setStyleSheet(u"QPushButton {\n"
                               "	border: 1px;\n"
                               "	background-color: rgb(20,20,20);\n"
                               "	color: rgb(255, 255, 255);\n"
                               "}\n"
                               "\n"
                               "QPushButton:hover {\n"
                               "	background-color: rgb(30,30,30);\n"
                               "	color: rgb(255, 255, 255);\n"
                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "	background-color: rgb(200,200,200);\n"
                               "	color: rgb(30, 30, 30);\n"
                               "}")
        self.two.setFlat(True)
        self.two.clicked.connect(lambda: self.number_button_press(u"2"))

        self.gridLayout.addWidget(self.two, 4, 1, 1, 1)

        self.three = QPushButton(self.layoutWidget)
        self.three.setObjectName(u"three")
        self.three.setEnabled(True)
        sizePolicy.setHeightForWidth(self.three.sizePolicy().hasHeightForWidth())
        self.three.setSizePolicy(sizePolicy)
        self.three.setMaximumSize(QSize(60, 60))
        self.three.setFont(font)
        self.three.setAutoFillBackground(False)
        self.three.setStyleSheet(u"QPushButton {\n"
                                 "	border: 1px;\n"
                                 "	background-color: rgb(20,20,20);\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "	background-color: rgb(30,30,30);\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "	background-color: rgb(200,200,200);\n"
                                 "	color: rgb(30, 30, 30);\n"
                                 "}")
        self.three.setFlat(True)
        self.three.clicked.connect(lambda: self.number_button_press(u"3"))

        self.gridLayout.addWidget(self.three, 4, 2, 1, 1)

        self.plus = QPushButton(self.layoutWidget)
        self.plus.setObjectName(u"plus")
        self.plus.setEnabled(True)
        sizePolicy.setHeightForWidth(self.plus.sizePolicy().hasHeightForWidth())
        self.plus.setSizePolicy(sizePolicy)
        self.plus.setMaximumSize(QSize(60, 60))
        self.plus.setFont(font)
        self.plus.setAutoFillBackground(False)
        self.plus.setStyleSheet(u"QPushButton {\n"
                                "	border: 1px;\n"
                                "	background-color: rgb(20,20,20);\n"
                                "	color: rgb(255, 255, 255);\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "	background-color: rgb(30,30,30);\n"
                                "	color: rgb(255, 255, 255);\n"
                                "}\n"
                                "\n"
                                "QPushButton:pressed {\n"
                                "	background-color: rgb(200,200,200);\n"
                                "	color: rgb(30, 30, 30);\n"
                                "}")
        self.plus.setFlat(True)
        self.plus.clicked.connect(lambda: self.function_button_press(self.input, "plus"))

        self.gridLayout.addWidget(self.plus, 4, 3, 1, 1)

        self.minus = QPushButton(self.layoutWidget)
        self.minus.setObjectName(u"minus")
        self.minus.setEnabled(True)
        sizePolicy.setHeightForWidth(self.minus.sizePolicy().hasHeightForWidth())
        self.minus.setSizePolicy(sizePolicy)
        self.minus.setMaximumSize(QSize(60, 60))
        self.minus.setFont(font)
        self.minus.setAutoFillBackground(False)
        self.minus.setStyleSheet(u"QPushButton {\n"
                                 "	border: 1px;\n"
                                 "	background-color: rgb(20,20,20);\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "	background-color: rgb(30,30,30);\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "	background-color: rgb(200,200,200);\n"
                                 "	color: rgb(30, 30, 30);\n"
                                 "}")
        self.minus.setFlat(True)
        self.minus.clicked.connect(lambda: self.decide_minus())

        self.gridLayout.addWidget(self.minus, 4, 4, 1, 1)

        self.comma = QPushButton(self.layoutWidget)
        self.comma.setObjectName(u"comma")
        self.comma.setEnabled(True)
        sizePolicy.setHeightForWidth(self.comma.sizePolicy().hasHeightForWidth())
        self.comma.setSizePolicy(sizePolicy)
        self.comma.setMaximumSize(QSize(60, 60))
        self.comma.setFont(font)
        self.comma.setAutoFillBackground(False)
        self.comma.setStyleSheet(u"QPushButton {\n"
                                 "	border: 1px;\n"
                                 "	background-color: rgb(20,20,20);\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "	background-color: rgb(30,30,30);\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "	background-color: rgb(200,200,200);\n"
                                 "	color: rgb(30, 30, 30);\n"
                                 "}")
        self.comma.setFlat(True)
        self.comma.clicked.connect(lambda: self.number_button_press(u","))

        self.gridLayout.addWidget(self.comma, 5, 0, 1, 1)

        self.zero = QPushButton(self.layoutWidget)
        self.zero.setObjectName(u"zero")
        self.zero.setEnabled(True)
        sizePolicy.setHeightForWidth(self.zero.sizePolicy().hasHeightForWidth())
        self.zero.setSizePolicy(sizePolicy)
        self.zero.setMaximumSize(QSize(60, 60))
        self.zero.setFont(font)
        self.zero.setAutoFillBackground(False)
        self.zero.setStyleSheet(u"QPushButton {\n"
                                "	border: 1px;\n"
                                "	background-color: rgb(20,20,20);\n"
                                "	color: rgb(255, 255, 255);\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "	background-color: rgb(30,30,30);\n"
                                "	color: rgb(255, 255, 255);\n"
                                "}\n"
                                "\n"
                                "QPushButton:pressed {\n"
                                "	background-color: rgb(200,200,200);\n"
                                "	color: rgb(30, 30, 30);\n"
                                "}")
        self.zero.setFlat(True)
        self.zero.clicked.connect(lambda: self.number_button_press(u"0"))

        self.gridLayout.addWidget(self.zero, 5, 1, 1, 1)

        self.Ans = QPushButton(self.layoutWidget)
        self.Ans.setObjectName(u"Ans")
        self.Ans.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Ans.sizePolicy().hasHeightForWidth())
        self.Ans.setSizePolicy(sizePolicy)
        self.Ans.setMaximumSize(QSize(60, 60))
        self.Ans.setFont(font)
        self.Ans.setAutoFillBackground(False)
        self.Ans.setStyleSheet(u"QPushButton {\n"
                               "	border: 1px;\n"
                               "	background-color: rgb(20,20,20);\n"
                               "	color: rgb(255, 255, 255);\n"
                               "}\n"
                               "\n"
                               "QPushButton:hover {\n"
                               "	background-color: rgb(30,30,30);\n"
                               "	color: rgb(255, 255, 255);\n"
                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "	background-color: rgb(200,200,200);\n"
                               "	color: rgb(30, 30, 30);\n"
                               "}")
        self.Ans.setFlat(True)
        self.Ans.clicked.connect(lambda: self.function_button_press(self.input, "ans"))

        self.gridLayout.addWidget(self.Ans, 5, 2, 1, 1)

        self.equals = QPushButton(self.layoutWidget)
        self.equals.setObjectName(u"equals")
        self.equals.setEnabled(True)
        sizePolicy.setHeightForWidth(self.equals.sizePolicy().hasHeightForWidth())
        self.equals.setSizePolicy(sizePolicy)
        self.equals.setMaximumSize(QSize(60, 60))
        self.equals.setFont(font)
        self.equals.setAutoFillBackground(False)
        self.equals.setStyleSheet(u"QPushButton {\n"
                                  "	border: 1px;\n"
                                  "	background-color: rgb(20,20,20);\n"
                                  "	color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover {\n"
                                  "	background-color: rgb(30,30,30);\n"
                                  "	color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:pressed {\n"
                                  "	background-color: rgb(200,200,200);\n"
                                  "	color: rgb(30, 30, 30);\n"
                                  "}")
        self.equals.setFlat(True)
        self.equals.clicked.connect(lambda: self.function_button_press(self.input, "equals"))

        self.gridLayout.addWidget(self.equals, 5, 3, 1, 1)

        self.guide = QPushButton(self.layoutWidget)
        self.guide.setObjectName(u"guide")
        self.guide.setEnabled(True)
        sizePolicy.setHeightForWidth(self.guide.sizePolicy().hasHeightForWidth())
        self.guide.setSizePolicy(sizePolicy)
        self.guide.setMaximumSize(QSize(60, 60))
        self.guide.setFont(font)
        self.guide.setAutoFillBackground(False)
        self.guide.setStyleSheet(u"QPushButton {\n"
                                 "	border: 1px;\n"
                                 "	background-color: rgb(160,160,160);\n"
                                 "	color: rgb(0, 0, 0);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "	background-color: rgb(50,50,50);\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "	background-color: rgb(30,30,30);\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "}")
        self.guide.setFlat(True)
        self.guide.clicked.connect(lambda: webbrowser.open_new(self.doc_path))

        self.gridLayout.addWidget(self.guide, 5, 4, 1, 1)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 441, 133))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.buffer_label = QLabel(self.layoutWidget1)
        self.buffer_label.setObjectName(u"buffer_label")
        self.buffer_label.setMaximumSize(QSize(400, 100))
        font1 = QFont()
        font1.setPointSize(15)
        self.buffer_label.setFont(font1)
        self.buffer_label.setLayoutDirection(Qt.LeftToRight)
        self.buffer_label.setStyleSheet(u"QLabel {\n"
                                        "	color: rgb(255,255,255)\n"
                                        "}")
        self.buffer_label.setTextFormat(Qt.RichText)
        self.buffer_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.buffer_label.setMargin(15)

        self.verticalLayout.addWidget(self.buffer_label)

        self.action_label = QLabel(self.layoutWidget1)
        self.action_label.setObjectName(u"action_label")
        self.action_label.setMaximumSize(QSize(400, 100))
        self.action_label.setFont(font)
        self.action_label.setLayoutDirection(Qt.LeftToRight)
        self.action_label.setStyleSheet(u"QLabel {\n"
                                        "	color: rgb(255,255,255)\n"
                                        "}")
        self.action_label.setTextFormat(Qt.RichText)
        self.action_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.action_label.setMargin(15)

        self.verticalLayout.addWidget(self.action_label)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 23))
        self.menubar.setStyleSheet(u"QMenuBar {\n"
                                   "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
                                   "        stop:0 rgb(50,50,50), stop:1 rgb(40,40,40));\n"
                                   "}\n"
                                   "QMenuBar::item {\n"
                                   "    spacing: 3px;           \n"
                                   "    padding: 2px 10px;\n"
                                   "    color: rgb(255,255,255);  \n"
                                   "}\n"
                                   "QMenuBar::item:selected {    \n"
                                   "    background-color: rgb(80,80,80);\n"
                                   "}\n"
                                   "QMenuBar::item:pressed {\n"
                                   "    background: rgb(120,120,120);\n"
                                   "}")
        self.menuasd = QMenu(self.menubar)
        self.menuasd.setObjectName(u"menuasd")
        self.menuasd.setStyleSheet(u"QMenu {\n"
                                   "	color: rgb(255,255,255);\n"
                                   "}")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.actionNapoveda = QAction(mainWindow)
        self.actionNapoveda.setObjectName(u"actionNapoveda")
        self.actionNapoveda.triggered.connect(lambda: webbrowser.open_new(self.guide_path))
        self.actionManual = QAction(mainWindow)
        self.actionManual.setObjectName(u"actionDokumentace")
        self.actionManual.triggered.connect(lambda: webbrowser.open_new(self.doc_path))

        self.menubar.addAction(self.menuasd.menuAction())

        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuasd.menuAction())
        self.menuasd.addSeparator()
        self.menuasd.addAction(self.actionManual)
        self.menuasd.addSeparator()
        self.menuasd.addAction(self.actionNapoveda)

        self.retranslateUi(mainWindow)

        self.xpowery.setDefault(False)

        QMetaObject.connectSlotsByName(mainWindow)

    ##
    # @brief Nastaví texty elementů aplikace
    #
    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"FitCalcPro", None))
        self.actionManual.setText(QCoreApplication.translate("mainWindow", u"Manu\u00E1l", None))
        self.actionNapoveda.setText(QCoreApplication.translate("mainWindow", u"N\u00e1pov\u011bda", None))
        self.xpowery.setText(QCoreApplication.translate("mainWindow", u"x\u02b8", None))
        self.yrootx.setText(QCoreApplication.translate("mainWindow", u"\u02b8\u221ax", None))
        self.twopowerx.setText(QCoreApplication.translate("mainWindow", u"x\u00b2", None))
        self.tworootx.setText(QCoreApplication.translate("mainWindow", u"\u00b2\u221ax", None))
        self.factorial.setText(QCoreApplication.translate("mainWindow", u"n!", None))
        self.invertor.setText(QCoreApplication.translate("mainWindow", u"+/-", None))
        self.sin.setText(QCoreApplication.translate("mainWindow", u"sin", None))
        self.cos.setText(QCoreApplication.translate("mainWindow", u"cos", None))
        self.tan.setText(QCoreApplication.translate("mainWindow", u"tan", None))
        self.pi.setText(QCoreApplication.translate("mainWindow", u"\u03c0", None))
        self.seven.setText(QCoreApplication.translate("mainWindow", u"7", None))
        self.eight.setText(QCoreApplication.translate("mainWindow", u"8", None))
        self.nine.setText(QCoreApplication.translate("mainWindow", u"9", None))
        self.ac.setText(QCoreApplication.translate("mainWindow", u"AC", None))
        self.delete.setText(QCoreApplication.translate("mainWindow", u"DEL", None))
        self.four.setText(QCoreApplication.translate("mainWindow", u"4", None))
        self.five.setText(QCoreApplication.translate("mainWindow", u"5", None))
        self.six.setText(QCoreApplication.translate("mainWindow", u"6", None))
        self.times.setText(QCoreApplication.translate("mainWindow", u"x", None))
        self.devide.setText(QCoreApplication.translate("mainWindow", u"/", None))
        self.one.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.two.setText(QCoreApplication.translate("mainWindow", u"2", None))
        self.three.setText(QCoreApplication.translate("mainWindow", u"3", None))
        self.plus.setText(QCoreApplication.translate("mainWindow", u"+", None))
        self.minus.setText(QCoreApplication.translate("mainWindow", u"-", None))
        self.comma.setText(QCoreApplication.translate("mainWindow", u",", None))
        self.zero.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.Ans.setText(QCoreApplication.translate("mainWindow", u"Ans", None))
        self.equals.setText(QCoreApplication.translate("mainWindow", u"=", None))
        self.guide.setText(QCoreApplication.translate("mainWindow", u"???", None))
        self.buffer_label.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.action_label.setText(QCoreApplication.translate("mainWindow", u"Zadejte p\u0159\u00edklad", None))
        self.menuasd.setTitle(QCoreApplication.translate("mainWindow", u"N\u00e1pov\u011bda"))
