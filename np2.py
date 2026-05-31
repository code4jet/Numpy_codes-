import numpy as np
#  How to make transpose matrics 
a=np.array([[4,5,5,6,3,5]])
b=np.array([
    [2,8,9],
    [1,7,9],
    [6,7,4],
    [8,2,6]
])
print(a.shape)
print(b.shape)
print(a.T)
print(b.T)
print((a.T).shape)
print((b.T).shape)
