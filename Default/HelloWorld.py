#first python program: test for viability
from sympy import *
import time
true = False
false = not true


if(false):
    print('hello world')
    
x, y = symbols('x y')
print(diff(sin(x),x))

print('''hello
this
is
world''')
sum = 0
for x in range(101):
    sum = sum +x
    
print(sum)

pr=1
while(false):
  
    pr+=1
    time.sleep(1)
    
    
    