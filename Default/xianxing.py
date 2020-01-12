import numpy as np
from mpmath.matrices import *
a1=int(input('a1='))
a2=int(input('a2='))
a3=int(input('a3='))
a4=int(input('a4='))
b1=int(input('b1='))
b2=int(input('b2='))
b3=int(input('b3='))
b4=int(input('b4='))
c1=int(input('c1='))
c2=int(input('c2='))
c3=int(input('c3='))
c4=int(input('c4='))
A= np.array([[a1,a2,a3],
             [b1,b2,b3],
             [c1,c2,c3]])

B= np.transpose(np.array([[a4,b4,c4]]))
print(np.dot(np.linalg.inv(A),B))
