##
# @file math_interpreter.py
# @brief Interpretuje matematický výraz
# @author Miroslav Šafář <xsafar23.stud.fit.vutbr.cz>
#
# * Project: fit-ivs-2
# * Date created: 2021-03-29
# * Last modified: 2021-04-23
#

import math_lib


##
# @brief Vyčíslí výraz dle priority operací a vrátí jeho hodnotu
# @param members List členů výrazu
# @param operations List operací mezi členy
# @return Výsledná hodnota výrazu
#
def eval(members, operations):
    i = 0
    while i < len(operations):
        if operations[i] == "power":
            members[i] = math_lib.power(members[i], members[i + 1])
            del members[i + 1]
            del operations[i]
        elif operations[i] == "root":
            members[i] = math_lib.nth_root(members[i + 1], members[i])
            del members[i + 1]
            del operations[i]
        else:
            i = i + 1

    i = 0
    while i < len(operations):
        if operations[i] == "*":
            members[i] = math_lib.multiply(members[i], members[i + 1])
            del members[i + 1]
            del operations[i]
        elif operations[i] == "/":
            members[i] = math_lib.divide(members[i], members[i + 1])
            del members[i + 1]
            del operations[i]
        else:
            i = i + 1

    i = 0
    while i < len(operations):
        if operations[i] == "+":
            members[i] = math_lib.sum(members[i], members[i + 1])
            del members[i + 1]
            del operations[i]
        elif operations[i] == "-":
            members[i] = math_lib.sub(members[i], members[i + 1])
            del members[i + 1]
            del operations[i]
        else:
            i = i + 1

    return members[0]
