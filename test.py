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

scores = np.array([80, 90, 70])
weights = np.array([1, 2, 1])   # mid-term counts double

x=np.average(scores)                       # → 80.0  (unweighted)
y=np.average(scores, weights=weights)      # → 82.5  (weighted)
z=np.average(scores, weights=weights, returned=False)  # → (82.5, 4.0)
print(x,y,z)

# NAN  and INF(infinity )
import numpy as np

x = np.array([1, 2, np.nan, 4])
print(np.mean(x))   # result is NaN 

print(np.nanmean(x)) # Ignore NaN
y = np.array([1, 0, -1])
  # [1.0, inf, -1.0]
print(1 / y) 
print(type(np.inf))

