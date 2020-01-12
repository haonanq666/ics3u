from mpmath import matrix
from mpmath import sin, cos, pi


def rochelimitfluid(satellite, body):
    #this function calculates the fluid roche limit between the body and the satellite
    densratio = dens[body]/dens[satellite]
    limfluid = 2.44*rad[body]*((densratio)**(1/3))
    return limfluid
    
def rochelimitrigid(satellite, body):
    #same as above, rigid roche limit for satellite and body
    densratio = dens[body]/dens[satellite]
    limrigid = 1.26*rad[body]*((densratio)**(1/3))
    return limrigid

def gravityforce(body1,body2,centerdistance):
    #calculates the force of gravity between two bodies
    force = (6.674184*(10**(-11))*masses[body1]*masses[body2])/centerdistance**2
    return force

def vectorize(magnitude, angle):
    #this function takes the magnitude and angle and decomposes it into its components
    vector = matrix([magnitude*(cos(angle)),
                     magnitude*(sin(angle))])
    return vector

def angularvelocity(planet):
    #angular velocity of planets in rad/s
    angv = -2*pi/orbperiod[planet]
    return angv

planets = ('sun','mercury','venus','mars','saturn','uranus','neptune','jupiter','pluto')
#list of all planets excluding earth, including the sun

masses = {'sun':1.989*(10**30),'mercury':0.33*(10**24),'venus':4.87*(10**24),'earth':5.97*(10**24),'mars':0.642*(10**24),'saturn':568*(10**24),'uranus':86.8*(10**24),'neptune':102*(10**24),'jupiter':1898*(10**24),'pluto':0.0146*(10**24)}  
#mass of planets in kg

dens = {'sun':1410,'mercury':5427,'venus':5243,'earth':5514,'mars':3933,'saturn':687,'uranus':1271,'neptune':1638,'jupiter':1326,'pluto':2095}
#density of planets in kg/m^3

rad = {'sun':6.69*(10**8),'mercury':2.43*(10**6),'venus':6.06*(10**6),'earth':6.37*(10**6),'mars':3.37*(10**6),'saturn':5.85*(10**7),'uranus':2.33*(10**7),'neptune':2.21*(10**7),'jupiter':7.1492*(10**7),'pluto':1195000}  
#radius of planets in m

orbrad = {'mercury':57.9*(10**3)*(10**6),'venus':108.2*(10**3)*(10**6),'earth':149.6*(10**3)*(10**6),'mars':227.9*(10**3)*(10**6),'saturn':1433.5*(10**3)*(10**6),'uranus':2872.5*(10**3)*(10**6),'neptune':4495.1*(10**3)*(10**6),'jupiter':778.6*(10**3)*(10**6),'pluto':5906.4*(10**3)*(10**6)} 
#orbital radius of planets in m 

orbperiod = {'mercury':88*24*3600,'venus':224.7*24*3600,'earth':0,'mars':687*24*3600,'saturn':10747*24*3600,'uranus':30589*24*3600,'neptune':59800*24*3600,'jupiter':4331*24*3600,'pluto':90560*24*3600} 
# orbital period in seconds 

tonneforce = 9806.65 #newtons
#this is a conversion factor, 1 tonneforce is that many newtons

xxfdj= 500000000000000000*tonneforce 
#this variable defines the maximum propulsion force possible for the earth

