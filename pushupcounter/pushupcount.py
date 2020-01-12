import time as t
from math import sqrt 


def pushup (initial, day):
    #calculates the amount of pushups due 
    return (initial*(2**(day-1)))

try:
#to prevent an error being thrown if user inputs non integer inputs
    ini = int(input('initial number of pushups: \n'))
    
    sqrt(ini)
    #this checks if ini is positive. Make sure to use math.sqrt, not cmath.sqrt 
    #as cmath.sqrt() supports complex roots, thus no exception will be thrown
    
    time = int(input('how many days has student not handed in (first day of pushups is day 1): \n'))
    amount = pushup(ini, time)
    
    
    print('calculating...')
    for x in range(10):
        #prints a fake progress bar and a simulated calculation delay
        print(u'\u25A0', end="")
        t.sleep(1)
             
    print('\n')
    print('pushups due: %d'%amount)
    
    years = (amount/2806)/8765.82 
    #calculates the number of years it would take to do that 
    #many pushups, at world record speed
    
    if(years>1):
        #prints a warning if it would take more than one year (theoretically) to do the pushups
        print('')
        print('''The current world record for most pushups in one hour is
held by Jarrad Young. He completed 2806 in one hour. 
At this rate, it will take you %f years'''%years)
    
    elif(amount>=46001):
        #if time is less than a year, but the number of pushups exceeds the world record for pushups in
        #24 hours, this warning is given
        print('')
        print('''Note that the current world record for number of push ups in 24 hours
(with rest periods allowed in between) is held by Charles Servizio. He 
completed 46001.''')

except ValueError:
    #if user inputs illegal data, this will happen
    print('')
    print('illegal input')

except OverflowError:
    #if the number is too large to calculate
    print('')
    print('Number too large to be calculated.')





