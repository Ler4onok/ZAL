from itertools import zip_longest
import operator

def polyEval(poly, x):
    quantity = len(poly)
    sum = 0
    for i in range(quantity):
        sum += poly[i]* (x**i)
    return sum


def polySum(poly1, poly2):
    poly3 =[sum(x) for x in zip_longest(poly1, poly2, fillvalue=0)]
    for i in range(len(poly3)):
        if poly3[-1] == 0 or poly3[-1] == 0.0:
            poly3.pop()
    return poly3


def polyMultiply(poly1, poly2):
    poly3 = []
    i, j = 0, 0
    while i < ((len(poly1)-1) * (len(poly2)-1)):
        poly3.append(0)
        i += 1
    i = 0
    while i < len(poly1):
        while j < len(poly2):
            poly3[i+j] += poly1[i] * poly2[j]
            j += 1
        i += 1
        j = 0
    i = (len(poly3)-1)
    while poly3[i] == 0:
        del poly3[i]
        i -= 1
    return poly3



