import pygame
import sys
import mpmath as mp
from wanderingearth.wanderfunctions import orbrad, planets, rochelimitfluid, xxfdj, vectorize
from wanderingearth.ins import updateposition, absposition, zero, distance
from math import sqrt, atan2
from mpmath import matrix, pi
from sympy.plotting.intervalmath.interval_arithmetic import interval


x=0
y=1
#defined to ease calling out x, y vector components

def scaletowindow(pointoriginal):
    #This function accepts a position vector and output the Pygame coordinates
    #origin is in center of screen
    point = scalematrix*pointoriginal
    windowx = point[x] + screenwidth/2 
    windowy = screenheight/2 - point[y]
    return mp.matrix([[windowx],
                      [windowy]])

def blitplanet(planet):
    #This function draws the planet onto the window
    if(planet == 'earth'):
        point = scaletowindow(positionearth)
        gameconsole.blit(earth, (point[x], point[y]))
    
    else: 
        point = scaletowindow(absposition(planet))
        if(planet == 'sun'):
            gameconsole.blit(sun, (point[x], point[y]))
        else:    
            gameconsole.blit(planet1, (point[x], point[y]))
        
def intro():
    #introduction screen when user first opens the program
    while(True):
        gameconsole.fill(black)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_ESCAPE):
                    #exit on escape key
                    sys.exit()
                if(event.key == pygame.K_SPACE):
                    #starts on space key
                    rungame()
        title = datafont.render('The Wandering Earth', False, white)
        line1 = smallfont.render('use the arrow keys to drive earth and escape the solar system', False, white)
        line2 = smallfont.render('press space to start', False, white)
        
        gameconsole.blit(title, (440, 100))
        gameconsole.blit(line1, (300, 200))
        gameconsole.blit(line2, (500, 300))
        gameconsole.blit(warningtext, (500, 400))
        pygame.display.update()
        
        

def ending():
    #ending page
    while(True):
        gameconsole.fill(black)
        restart = datafont.render('press space to restart', False, white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_ESCAPE):
                    #exit on escape 
                    sys.exit()
                if(event.key == pygame.K_SPACE):
                    #restart on space
                    pygame.mixer.music.stop()
                    rungame()
        
        if(safe == 0):
            #successful game completion
            safe0 = datafont.render("you have escaped the solar system!", False, white)
            gameconsole.blit(safe0, (200, 100))
        elif(safe == 1):
            #disintegration due to entering Roche limit
            safe1 =  datafont.render("you have entered the Roche limit of another planet. You died.", False, white)
            gameconsole.blit(safe1, (200, 100))
        elif(safe == 2):
            #burning due to too close to the sun
            safe2 = datafont.render("you have been too close to the sun. You died.", False, white)
            gameconsole.blit(safe2, (200, 100))
        gameconsole.blit(restart, (300, 200))
        pygame.display.update()
        
def rungame():
    global scalematrix, positionearth, safe, propulsion
    
    pygame.mixer.music.play(-1)#plays the background music

    zero()
    safe = 0
    #determines state of the game when ending() is called (success or what type of death)
    
    propulsion = matrix([[0],
                         [0]])
    
    
    planetrad = 'saturn'
    #the planet's radius which to scale the window to

    while True:
        positionearth = updateposition(propulsion)
       
        scale = ((screenheight-10)/2)/orbrad[planetrad]
        scalematrix = mp.matrix([[scale,0],
                                 [0,    scale]]) 
        
        earthwindowpos = scaletowindow(positionearth)
        
        
        if(planetrad == 'saturn'):
            #rescales if the earth leaves the screen while scaled to saturn
            if(earthwindowpos[x]<0)or(earthwindowpos[x]>screenwidth)or(earthwindowpos[y]<0)or(earthwindowpos[y]>screenheight):
                planetrad = 'pluto'
        elif(planetrad == 'pluto'):
            #ends game if earth leaves the screen when scaled to pluto
            if(earthwindowpos[x]<0)or(earthwindowpos[x]>screenwidth)or(earthwindowpos[y]<0)or(earthwindowpos[y]>screenheight):
                ending()
            
        #checks for user input    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_ESCAPE):
                    sys.exit()
                    
        
    
        #clears window then redraws all planets in new positions
        gameconsole.fill(black)
        blitplanet('earth')
        for planet in planets:
            blitplanet(planet)
         
        checksafe()
        updatepropulsion()
        
        #text in upper left corner showing propulsion and angle
        flightdata = datafont.render("propulsion %d N" %(sqrt(propulsion[x]**2+propulsion[y]**2)), False, (white))
        flightdata2 = datafont.render("angle %d" %(angle*(360/(2*pi))), False, white)
        gameconsole.blit(flightdata, (10,10))
        gameconsole.blit(flightdata2, (10, 60))
        
        #draws arrow that points in direction of thrust (force on earth is opposite of this arrow)
        gameconsole.blit( pygame.transform.rotate(arrow, angle*(360/(2*pi))), (100, 120))
        
        pygame.display.update()
    

def checksafe():
    #checks for conditions of game failure
    global safe
    for planet in planets:
        if(distance(planet)<rochelimitfluid('earth', planet)):
        #checks if entered Roche limit
            safe = 1
            ending()
            return
    
    if(distance('sun') < 100000000000):
        #check if the earth is too close to the sun
        safe = 2
        ending()
        return

def updatepropulsion():
    #gets the new propulsion (as updated by the user)
    global propulsion, prop, angle
    keys = pygame.key.get_pressed()
    prop = sqrt(propulsion[x]**2 + propulsion[y]**2)
    angle = atan2(propulsion[y],propulsion[x])
    
    
    #checks for user input on keyboard and changes the angle or magnitude of propulsion
    if(keys[pygame.K_UP]):
            if(prop+ xxfdj/100 in interval(0,xxfdj)):
                #checks if the increasing by a certain increment will exceed the maximum allowed
                prop += xxfdj/100
            else:
                #makes it the maximum allowed if cannot increase by set increment
                prop = xxfdj
    if(keys[pygame.K_DOWN]):
            if (prop-xxfdj/100 in interval(0, xxfdj)):
                #same logic as above
                prop+= -xxfdj/100
            else:
                prop = 0
    if(keys[pygame.K_LEFT]):
        if(angle + pi/70<= 2*pi):
            angle += pi/70
    if(keys[pygame.K_RIGHT]):
        if(angle - pi/70 >= -2*pi):
            #angle lower limit is -2pi because the third and fourth quadrants are expressed as negative angles
            angle += -pi/70
    propulsion = vectorize(prop, angle)
    

#initializes pygame and font
pygame.init()
pygame.font.init()

#defines fonts, colors, etc. to be rendered on window
datafont = pygame.font.SysFont('Comic Sans MS', 50)
smallfont = pygame.font.SysFont('Comic Sans MS', 30)
white = (255,255,255)
black = (0,0,0)
screenwidth, screenheight = pygame.display.Info().current_w, pygame.display.Info().current_h
gameconsole = pygame.display.set_mode((screenwidth, screenheight), pygame.FULLSCREEN)
pygame.mouse.set_visible(False) #Hides the mouse so it doesn't appear on screen 



#loads the files necessary for the program
planet1 = pygame.image.load('planet.png')#generic planet for all planets other than earth and sun
earth = pygame.image.load('earth.png')
sun = pygame.image.load('sun.png')
arrow = pygame.image.load('arrow.png')
warningtext = pygame.image.load('warning.png') #for introduction screen, is an image of text
bgm = pygame.mixer.music.load('bgm.wav') #background music for game

#incorrect sRGB warning will be thrown because images create in Photoshop RGB. 
#This does not affect the program


#starts by calling the introduction screen
intro()








