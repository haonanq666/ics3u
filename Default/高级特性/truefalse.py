import random
true = True
false = False
if(random.randint(1,100)<31):
    true = False
    false = True

if(false):
    print('inverted')
    
else:
    print('not inverted')