import formulas
import factor
import conversions
from math import tan, sqrt
from math import pi as mpi

pi = mpi


def prime_check(n):
    factors = []
    for i in range(n + 1):
        if i != 0 and n % i == 0:
            factors.append(i)
    if len(factors) == 2:
        return True
    else:
        return False


def odd_even_checker(number):
    if number % 2 == 0:
        return "even"
    elif number % 2 == 1:
        return "odd"
    else:
        return "Invalid number"


def square(number):
    return number * number


def cube(number):
    return pow(number, 3)


def find_distance_2_coor(x1, x2, y1, y2):
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


def pythagoras(base_square, perpendicular_square):
    hypotenusesq = base_square + perpendicular_square
    hypotenuse = sqrt(hypotenusesq)
    return hypotenuse


def fibonacci(n):
    thelist = [1, 1]
    while len(thelist) != n:
        thelist.append(thelist[-1] + thelist[-2])
    return thelist


def cuberoot(x):  # Only Compatible with perfect cubes
    for ans in range(0, abs(x) + 1):
        if ans ** 3 == abs(x):
            break
    if ans ** 3 != abs(x):
        return 'Not a perfect cube'
    else:
        if x < 0:
            ans = -ans
    return ans


def to_the_power_anything_root(to_the_power_of_what, number):
    for ans in range(0, abs(number) + 1):
        if ans ** to_the_power_of_what == abs(number):
            break
    if ans ** to_the_power_of_what != abs(number):
        return 'Not perfect'
    else:
        if number < 0:
            ans = -ans
    return ans


def profit_percent_calculator(investment, output):
    profit_or_loss_amount = output - investment
    if profit_or_loss_amount >= 0:
        profit_or_loss = 'profit'
    elif profit_or_loss_amount < 0:
        profit_or_loss = 'loss'
    else:
        return 'Invalid Inputs'
    if profit_or_loss == 'profit':
        return str((profit_or_loss_amount / investment * 100)) + '% Profit'
    elif profit_or_loss == 'loss':
        return str((abs(profit_or_loss_amount) / investment * 100)) + '% Loss'


def average(listofvalues):
    return sum(listofvalues) / len(listofvalues)


def average2(*args):
    listofvalues = []
    for item in args:
        listofvalues.append(item)
    return sum(listofvalues) / len(listofvalues)


def tow(base, mod):
    """Example: tow(10, 4) will return 10 to the power 10 to the power 10 to the power 10"""
    output = base
    for i in range(mod - 1):
        output = pow(output, base)
    return output


def is_decimal(n):
    x = type(n)
    x = str(x)
    if x == "<class 'float'>":
        return True
    else:
        return False


def is_square(n):
    num = sqrt(n)
    num = str(num)
    if num.endswith('.0'):
        return True
    return False


def is_integer(num):
    if isinstance(num, float):
        return num.is_integer()
    elif isinstance(num, int):
        return True
    else:
        return False
