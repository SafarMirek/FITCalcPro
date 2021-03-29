##
# @file profiling.py
# @brief Program určený pro výpočet výběrové směrodatné odchylky pomocí funkcí
# matematické knihovny math_lib.py
# @author Michaela Pařilová <xparil04.stud.fit.vutbr.cz>
#
# * Project: fit-ivs-2
# * Date created: 2021-03-28
# * Last modified: 2021-03-29
#

import sys
from math_lib import sum, sub, multiply, divide, power, nth_root

if __name__ == '__main__':

    sigma: int = 0
    sigma_pow_2: int = 0
    n: int = 0

    content = sys.stdin.readlines()

    for line in content:
        for i in line:
            if i.isdigit():
                sigma = sum(sigma, int(i))
                sigma_pow_2 = sum(power(int(i), 2), sigma_pow_2)
                n = sum(n, 1)

    x = divide(sigma, n)
    s = nth_root(multiply(divide(1, sub(n, 1)), sub(sigma_pow_2, multiply(n, power(x, 2)))), 2)

