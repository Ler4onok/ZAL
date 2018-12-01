
import math


def addition(x, y):
    addition_result = x + y
    return addition_result


def subtraction(x, y):
    subtraction_result = x - y
    return subtraction_result


def multiplication(x, y):
  #  multiplication_result = args[0]*args[1]
    multiplication_result = x * y
    return multiplication_result


def division(x, y):
    if y != 0:
        division_result = x/y
        return division_result
    else:
        raise ValueError('This operation is not supported for given input parameters')


def modulo(x, y):
    if 0 < y <= x:
        modulo_result = x % y
        return modulo_result
    else:
        raise ValueError('This operation is not supported for given input parameters')


def secondPower(x):
    secondPower_result = x * x
    return secondPower_result


def power(x, y):
    if y >= 0:
        power_result = x ** y
        return float(power_result)
    else:
        raise ValueError('This operation is not supported for given input parameters')


def secondRadix(x):
    if x > 0:
        secondRadix_result = math.sqrt(x)
        return secondRadix_result
    else:
        raise ValueError('This operation is not supported for given input parameters')


def magic(x, y, z, k):
    l = x + k
    m = y + z
    if m == 0:
        raise ValueError('This operation is not supported for given input parameters')
    z = ((l/m) + 1)
    return z


def control(a, x, y, z, k):
    if a == 'ADDITION':
        return addition(x, y)
    elif a == 'SUBTRACTION':
        return subtraction(x, y)
    elif a == 'MULTIPLICATION':
        return multiplication(x, y)
    elif a == 'DIVISION':
        return division(x, y)
    elif a == 'MOD':
        return modulo(x, y)
    elif a == 'POWER':
        return power(x, y)
    elif a == 'SECONDRADIX':
        return secondRadix(x)
    elif a == 'MAGIC':
        return magic(x, y, z, k)
    else:
        raise ValueError('This operation is not supported for given input parameters')

#print (control('SECONDRADIX', -3, 1, 1, 1))

