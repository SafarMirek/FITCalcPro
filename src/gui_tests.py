from PySide2 import QtCore

from gui import MainWindow

# TODO desetine cisla, errory, pravidla syntaxe

def test_clickable_numbers(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    qtbot.mouseClick(window.ui.one, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.ui.two, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.ui.three, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.ui.four, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.ui.five, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.ui.six, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.ui.seven, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.ui.eight, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.ui.nine, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.ui.zero, QtCore.Qt.LeftButton)

    assert window.ui.input == "1234567890"


def test_keyboard_numbers(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    result = "1"

    qtbot.keyPress(window, "1")
    assert window.ui.input == result

    for i in range(0, 9):
        result += str(i)
        qtbot.keyPress(window, str(i))

    assert window.ui.input == result


def test_clickable_operation_buttons(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    qtbot.mouseClick(window.ui.one, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.ui.plus, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.ui.one, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.ui.equals, QtCore.Qt.LeftButton)

    assert window.ui.input == "2"


def test_keyboard_operation_buttons(qtbot):
    pass
    #window = MainWindow()
    #qtbot.addWidget(window)
    #
    #for i in range(1, 10):
    #    qtbot.keyPress(i)
    #
    #    assert window.ui.input == "1234567890"


def test_basic_sum(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    qtbot.keyPress(window, "3")
    qtbot.keyPress(window, "+")
    qtbot.keyPress(window, "3")
    qtbot.mouseClick(window.ui.equals, QtCore.Qt.LeftButton)

    assert window.ui.input == "6"


def test_multiple_sum(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    qtbot.keyPress(window, "3")
    qtbot.keyPress(window, "+")
    qtbot.keyPress(window, "3")
    qtbot.keyPress(window, "+")
    qtbot.keyPress(window, "1")
    qtbot.mouseClick(window.ui.equals, QtCore.Qt.LeftButton)

    assert window.ui.input == "7"


def test_answer_variable(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    qtbot.keyPress(window, "3")
    qtbot.keyPress(window, "+")
    qtbot.keyPress(window, "3")
    qtbot.mouseClick(window.ui.equals, QtCore.Qt.LeftButton)

    qtbot.mouseClick(window.ui.ac, QtCore.Qt.LeftButton)

    qtbot.mouseClick(window.ui.Ans, QtCore.Qt.LeftButton)
    qtbot.keyPress(window, "*")
    qtbot.keyPress(window, "2")
    qtbot.mouseClick(window.ui.equals, QtCore.Qt.LeftButton)

    assert window.ui.input == "12"


def test_multiple_operation(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    qtbot.keyPress(window, "3")
    qtbot.keyPress(window, "-")
    qtbot.keyPress(window, "3")
    qtbot.keyPress(window, "+")
    qtbot.keyPress(window, "1")
    qtbot.keyPress(window, "*")
    qtbot.keyPress(window, "1")
    qtbot.keyPress(window, "6")
    qtbot.mouseClick(window.ui.tworootx, QtCore.Qt.LeftButton)
    qtbot.keyPress(window, "/")
    qtbot.keyPress(window, "2")
    qtbot.mouseClick(window.ui.twopowerx, QtCore.Qt.LeftButton)

    qtbot.mouseClick(window.ui.equals, QtCore.Qt.LeftButton)

    assert window.ui.input == "1"


def test_continuous_operation(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    qtbot.keyPress(window, "3")
    qtbot.keyPress(window, "+")
    qtbot.keyPress(window, "3")
    qtbot.mouseClick(window.ui.equals, QtCore.Qt.LeftButton)
    qtbot.keyPress(window, "*")
    qtbot.keyPress(window, "1")
    qtbot.keyPress(window, ".")
    qtbot.keyPress(window, "5")
    qtbot.mouseClick(window.ui.equals, QtCore.Qt.LeftButton)
    assert window.ui.input == "9"
    qtbot.keyPress(window, "/")
    qtbot.keyPress(window, "2")
    qtbot.mouseClick(window.ui.equals, QtCore.Qt.LeftButton)
    assert (window.ui.input == "4,5" or window.ui.input == "4.5")
    qtbot.keyPress(window, "*")
    qtbot.keyPress(window, "4")
    qtbot.mouseClick(window.ui.equals, QtCore.Qt.LeftButton)
    assert window.ui.input == "18"
    qtbot.keyPress(window, "-")
    qtbot.keyPress(window, "5")
    qtbot.mouseClick(window.ui.equals, QtCore.Qt.LeftButton)
    assert window.ui.input == "13"
    qtbot.keyPress(window, "+")
    qtbot.keyPress(window, "5")
    qtbot.mouseClick(window.ui.equals, QtCore.Qt.LeftButton)
    assert window.ui.input == "18"
    qtbot.keyPress(window, "-")
    qtbot.keyPress(window, "1")
    qtbot.keyPress(window, "6")
    qtbot.mouseClick(window.ui.equals, QtCore.Qt.LeftButton)
    assert window.ui.input == "2"
    qtbot.mouseClick(window.ui.twopowerx, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.ui.equals, QtCore.Qt.LeftButton)
    assert window.ui.input == "4"
    qtbot.mouseClick(window.ui.tworootx, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.ui.equals, QtCore.Qt.LeftButton)
    assert window.ui.input == "2"
