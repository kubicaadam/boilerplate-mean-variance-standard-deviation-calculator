import numpy as np

def calculate(list):

    a = np.array(list)

    a = np.reshape(a, (3,3))

    calculations = a

    return calculations

print(calculate([1,2,3,4,5,6,7,8,9]))