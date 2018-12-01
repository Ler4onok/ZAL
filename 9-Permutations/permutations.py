# import math

def permutations(array):

    list = []
    for i in array:
            array1 = array.copy()
            array1.remove(i)
            list.extend([[i] #recursion
            + ii for ii in permutations(array1)])

    if not array:
            return [[]]

    return list

#print(permutations([1]))
#print(permutations([1,2,3]))
