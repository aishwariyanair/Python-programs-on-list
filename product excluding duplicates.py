#Find product excluding duplicate

import numpy as np

a=[1,2,3,5,6,6,3]
b=list(set(a))
print(b)
mul=np.prod(b)
print('Product of list: ', mul)

