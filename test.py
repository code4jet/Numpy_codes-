import numpy as np
import sys
n=90
m=np.array([5])

print(type(n))
print(type(m))

print(sys.getsizeof(n))
print(sys.getsizeof(m[0]))

y=np.array([4.9,5.6,6.4,7.1],dtype=np.int32)
print(y)