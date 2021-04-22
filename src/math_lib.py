##
# @file math_lib.py
# @brief Matematická knihovna k druhému projektu do předmětu IVS
# @author Ondřej Kříž <xkrizo05.stud.fit.vutbr.cz>
#
# * Project: fit-ivs-2
# * Date created: 2021-03-07
# * Last modified: 2021-03-27
#

##
# @brief celočíselná konstanta určující počet des. míst po zaokrouhlení
#
accuracy = 10

##
# @brief konstanta Pi používaná pro výpočet úhlu v radiánech
#
pi = 3.141_592_653_589_793_238_462_643_383_279_502_884_197


##
# @brief Převede číslo zadané v úhlových stupních na radiány
# @param x Úhel ve stupních.
# @return Úhel v radiánech.
#
def to_rad(x):
    return x * pi / 180


##
# @brief Sečte dvě čísla.
# @param a První číslo.
# @param b Druhé číslo.
# @return Součet dvou čísel.
#
def sum(a, b):
    return a + b


##
# @brief Odečte druhé číslo od prvního.
# @param a První číslo.
# @param b Druhé číslo.
# @return Rozdíl dvou čísel.
#
def sub(a, b):
    return a - b


##
# @brief Vynásobí dvě čísla.
# @param a První číslo.
# @param b Druhé číslo.
# @return Součin dvou čísel.
#
def multiply(a, b):
    return round(a * b, accuracy)


##
# @brief Vydělí první číslo druhým číslem.
# @param a Dělenec.
# @param b Dělitel.
# @return Podíl dvou čísel.
# @exception ZeroDivisionError pokud se druhé číslo rovná nule.
#
def divide(a, b):
    if b == 0:
        raise ValueError

    ret = a / b
    return round(ret, accuracy)


##
# @brief Vypočítá faktoriál čísla.
# @param n Číslo, jehož faktoriál bude vypočten.
# @return Faktoriál čísla.
# @exception ValueError pokud číslo není přirozené nebo je nula.
#
def factorial(n):
    if n < 0 or not isinstance(n, int):
        raise ValueError

    num = 1
    if n == 0 or n == 1:
        return num
    while n != 1:
        num = num * n
        n = n - 1
    return num


##
# @brief Umocní číslo na exponent.
# @param a Základ mocniny.
# @param exp Exponent.
# @return Základ umocněný na exponent.
# @exception ValueError pokud exponent není celé číslo.
#
def power(a, exp):
    if not isinstance(exp, int):
        raise ValueError

    return a ** exp


##
# @brief Vypočíta n-tou odmocninu čísla.
# @param x Číslo pod odmocninou.
# @param n Řád odmocniny.
# @return N-tá odmocnina čísla.
# @exception ValueError pokud je řád odmocniny záporny sudý, není celočíselný, nebo je nula
#
def nth_root(x, n):
    if not isinstance(n, int) or n == 0:
        raise ValueError

    if x == 0:
        return x

    if x > 0:
        return round(x ** (1 / n), accuracy)

    if x < 0:
        if n % 2 == 0:
            raise ValueError
        return round(-((-x) ** (1 / float(n))), accuracy)


##
# @brief Vypočíta sinus čísla pomocí Taylorovy řady
# @param x Úhel ve stupních.
# @return Sinus úhlu.
# @see https://cs.wikipedia.org/wiki/Taylorova_%C5%99ada#Maclaurinova_%C5%99ada
#
def sin(x):
    x = x % 360
    # Převod úhlu na radiány
    x = to_rad(x)

    sine = 0
    step = 0
    prev = 1 - x
    k = x

    # k je další člen Taylorova polynomu. Je přičten nebo odečten podle aktuálního kroku.
    # Cyklus iteruje, dokud je přírůstková hodnota dostatečně velká, aby ji program zaznamenal
    while sine - prev != 0:
        prev = sine
        sine += power(-1, step) * k
        step += 1
        k = k * (x * x) / ((2 * step) * (2 * step + 1))

    return round(sine, accuracy)


##
# @brief Vypočíta cosinus čísla pomocí Taylorovy řady
# @param x Úhel ve stupních.
# @return Cosinus úhlu.
# @see https://cs.wikipedia.org/wiki/Taylorova_%C5%99ada#Maclaurinova_%C5%99ada
#
def cos(x):
    x = x % 360
    # Převod úhlu na radiány
    x = to_rad(x)

    cosx = 0
    step = 0
    prev = 1.4 - x
    k = 1

    # k je další člen Taylorova polynomu. Je přičten nebo odečten podle aktuálního kroku.
    # Cyklus iteruje, dokud je přírůstková hodnota dostatečně velká, aby ji program zaznamenal
    while cosx - prev != 0:
        prev = cosx
        cosx += power(-1, step) * k
        step += 1
        k = k * (x * x) / ((2 * step - 1) * (2 * step))

    return round(cosx, accuracy)


##
# @brief Vypočíta tangens čísla pomocí definičního vztahu
# @param x Úhel ve stupních.
# @return Tangens úhlu.
# @exception ValueError pokud je cosinus úhlu roven nule, neni tangens definován
#
def tan(x):
    sine = sin(x)
    cosx = cos(x)

    if cosx == 0:
        raise ValueError

    return sine / cosx
