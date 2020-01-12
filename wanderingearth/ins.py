from mpmath import matrix, sin, cos
from sympy.integrals.integrals import integrate
from builtins import sum
from sympy.core.symbol import symbols
from wanderingearth.wanderfunctions import angularvelocity, orbrad, masses, planets,\
    vectorize, gravityforce
from math import sqrt
from math import atan2





x=0
y=1
#to facilitate calling out vector elements x, y

interval = 100000
#this is the period of time when the acceleration is assumed to be constant
#larger interval means faster gameplay but less accuracy

def zero():
    #this function resets the initial position, velocity, and time variables; called when restarting
    global time, s0, v0   
    time = 0
    s0 = matrix([[orbrad['earth']],
                 [0]])

    v0 = matrix([[0],
                 [-30000]])

zero()

mass = masses['earth']
t = symbols('t')







def vectsum(*forces):
    #this function accepts any number of arguments and adds the vectors
    h= sum(forces)
    return h
    

def acceleration(mass, force):
    #this calculates the acceleration from Newton's equation
    a = force/mass
    return a

def velocity(v0, acc):
    #calculates velocity of earth by integrating the acceleration once
    vx= (integrate(acc[x], t)+v0[x]).evalf(subs={t:interval})
    vy= (integrate(acc[y], t)+v0[y]).evalf(subs={t:interval})
    v=matrix([[vx],
              [vy]])
    return v
    

def position(s0, v0, acc):
    #calculates position of earth by integrating acceleration twice
    dx = (integrate(integrate(acc[x], t)+v0[x])+s0[x]).evalf(subs={t:interval})
    dy = (integrate(integrate(acc[y], t)+v0[y])+s0[y]).evalf(subs={t:interval})  
    
    d = matrix([[dx],
                [dy]])
    return d

def updateposition(propulsion):
    #takes the propulsion force, and the gravity force exerted by other planets
    #and calculates the new position of earth 
    #Also updates the position velocity and time variables
    global s0, v0, time
    s0 = position(s0, v0, acceleration(mass, vectsum(netforce(), propulsion)))
    v0 = velocity(v0, acceleration(mass, vectsum(netforce(), propulsion)))
    time +=interval
    return s0
    
def absposition(planet):
    #this function is used to get the position of all planets other than the earth
    #it is assumed that they are perfectly circular in orbit
    if(planet == 'sun'):
        #the sun is always at the origin
        pos = matrix([[0],
                      [0]])
    else:
        angle = angularvelocity(planet)*time
        pos = matrix([[orbrad[planet]*cos(angle)], 
                      [orbrad[planet]*sin(angle)]])
    return pos
    
def netforce():
    #this function gets the net force acted on earth by all other planets
    F0= matrix([[0],
                [0]])
    for planet in planets:
        F= vectorize(forcemagnitude(planet), forcedir(planet))
        F0 = vectsum(F0,F)
    return F0

def distance(mubiao): 
    #distance between specified planet "mubiao" and earth
    dis = absposition(mubiao)-s0
    dist= sqrt(dis[x]**2+dis[y]**2)
    return dist

def forcemagnitude(mubiao): 
    #magnitude of force between specified planet "mubiao" and earth 
    mag= gravityforce(mubiao, 'earth', distance(mubiao))
    return mag
    
def forcedir(mubiao):
    #the direction of the specified planet "mubiao" from earth
    dis = absposition(mubiao)-s0
    direction = atan2(dis[y],dis[x])
    return direction

        
    




