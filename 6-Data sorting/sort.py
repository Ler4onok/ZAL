
from collections import OrderedDict


def sortNumbers(weights, condition):
    new_weights = []
    if condition=="ASC":
         new_weights = sorted(weights, key=int, reverse=False)

    if condition=="DESC":
        new_weights=sorted(weights, key=int, reverse=True)

    return new_weights




def sortData(weights, data, condition):

    if len(data) != len(weights):
        raise ValueError('Invalid input data')

    di = OrderedDict()
    for i in range( len( data ) ):
        di[data[i]] = weights[i]

    if condition == 'ASC':
        sorted_w = sorted( di.items(), key=lambda x: x[1] )
    else:
        sorted_w = sorted(di.items(), key=lambda x: x[1], reverse=True)

    new_w = []
    for i in range( len( weights ) ):
       new_w.append(sorted_w[i][0] )
    return new_w












