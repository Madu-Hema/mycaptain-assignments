string =input('enter the string:')
N=len(string)
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
x=most_frequent(string)
print('The order of frequency of string is:',x)
import operator
sorted_x = dict( sorted(x.items(), key=operator.itemgetter(1),reverse=True))
print('Decreasing order of frequency of string is:',sorted_x)
