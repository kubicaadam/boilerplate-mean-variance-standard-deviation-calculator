import numpy as np

def calculate(list):

    a = np.array(list)

    a = np.reshape(a, (3,3))

    calculations = {
        'mean': [a.mean(axis=0), a.mean(axis=1), a.mean()]
        #,
        #'variance': [axis1, axis2, flattened],
        #'standard deviation': [axis1, axis2, flattened],
        #'max': [axis1, axis2, flattened],
        #'min': [axis1, axis2, flattened],
        #'sum': [axis1, axis2, flattened]
    }

    return calculations

print(calculate([1,2,3,4,5,6,7,8,9]))