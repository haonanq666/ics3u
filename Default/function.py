
def factorial(a):
    fact = 1
    for x in range(a):
        fact = fact*(x+1)
        
    return fact

f=input('enter factorial: ')
print(factorial(int(f))) 
        

    
