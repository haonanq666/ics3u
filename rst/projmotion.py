from math import pi, log, sin, sqrt
import pygame

x=0
y=1


class railgun(object):
    '''class for railgun (player)'''
    def __init__(self, position, type):
        self.position = position
        self.image = type
        self.barrelAngle = 30
        self.barrelLength = 20
        self.barrelDiameter = 0.1
        self.railradius = 0.1
        self.shotsleft = 5
        self.shotmass = 4
    def getprojforce(self, current):
        '''gets force from current'''
        force = (((current**2)*(1.25663706*(10**-6)))/(2*pi))*log((self.barrelDiameter+self.railradius)/self.railradius)
        #magnetic field between two conducting rails is not constant.
        #integrated dF = IdLxB to arrive at this equation above.
        return float(force)
    def getprojmuzzlevel(self, current):
        '''gets muzzle velocity'''
        acc = (self.getprojforce(current))/self.shotmass
        v = sqrt(2*acc*self.barrelLength)
        return v
    def getrange(self, current, angle):
        '''get the range, in terms of how many pixels'''
        return 100*(((self.getprojmuzzlevel(current)/sqrt(50))**2)*sin(2*angle*(pi/180)))/9.81
        # divided by sqrt(50) to help scale the range onto the window (so as to not work with large numbers)
    

            
    
class target(object):
    '''red houses'''
    def __init__(self, location):
        self.location = location
        self.destroyed = False
        self.image = pygame.transform.scale(pygame.image.load('images/redhouse.png'), (50,50))
        self.rect = pygame.Rect(location, 630, 70, 50)
        self.destroyedimage = pygame.transform.scale(pygame.image.load('images/redhousedest.png'), (50,50))
    def isdestroyed(self, projectilerect):
        '''checks if house destroyed and updates self.destroyed'''
        if self.rect.colliderect(projectilerect):
            self.destroyed= True
        return self.destroyed
        
    def getimage(self):
        '''gets the image of house depending on destroyed statuss'''
        if self.destroyed == True:
            return self.destroyedimage
        else:
            return self.image
        
        
class nontarget(target):
    '''inherits target class, green houses'''
    def __init__(self, location):
        self.location = location
        self.destroyed = False
        self.image = pygame.transform.scale(pygame.image.load('images/greenhouse.png'), (50, 50))
        self.rect = pygame.Rect(location, 630, 50, 50)

        self.destroyedimage = pygame.transform.scale(pygame.image.load('images/greenhousedest.png'), (50, 50))
  
    
        
        
        
        
        
        
        
        
        