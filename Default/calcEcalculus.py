from sympy import Symbol, limit, oo
accuracy = input('please specify number of digits: \n')

if(accuracy.isdigit()==False):
    print('illegal input')
elif(int(accuracy)>0):
    x = Symbol('x')
    e = limit((1+1/x)**x,x,oo)
    print(e.evalf(accuracy))
else:
    print('illegal input')