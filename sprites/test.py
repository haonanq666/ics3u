import pygame
import sys
import time


pygame.init()
pygame.font.init()

class play(object):
    player = []
    #the array storing the sequence of player images
    
    for sprite in range(1, 7):
        player.insert(-1, pygame.image.load('nvren/'+str(sprite)+'.png'))
        
    leftplayer = player
    #creates a new array for storing reversed images of players (when walking backwards)
    leftplayer.reverse()

    
    def __init__(self):
        self.orientation = 'right'
        self.alive = True
        self.move = True
        self.dead = pygame.image.load('nvren/1sile.png')
        self.traveled = 0
        self.stepsback = 0
        self.position = self.traveled - self.stepsback
        #250x450 pixels is the player's size
def intro():
    while(True):
        
        display1.fill((0,0,0))
        introfont = myfont.render('The Great Patriotic War', False, (255,255,255))
        introfont2 = myfont.render('press space to start', False, (255,255,255))
        introfont3 = myfont.render('Not One Step Back -- Order No. 227', False, (255, 0 ,0))
       
        for introevent in pygame.event.get():
            if(introevent.type == pygame.KEYDOWN):
                if(introevent.key==pygame.K_SPACE):
                    return
                if(introevent.key == pygame.K_ESCAPE):
                    sys.exit()
        display1.blit(introfont, ( 250,100 ))
        display1.blit(introfont2, (250,300 ))
        display1.blit(introfont3, (50,500 ))
        pygame.display.update()

    
scr_width, scr_height = pygame.display.Info().current_w, pygame.display.Info().current_h
white = [255,255,255]  
black = [0,0,0]
display1 = pygame.display.set_mode((scr_width,scr_height), pygame.FULLSCREEN)
height = 200
jump = False
bob = play()
#bob is the player object
tank = pygame.transform.flip(pygame.image.load('nvren/t.png'), True, False)
tv = 0#tank velocity
position = [1400, 300]#initial position for tank
myfont = pygame.font.SysFont('Comic Sans MS', 70)

bolin = 2000 #distance to the target
spawntank = True
p = 550 #vertical coordinate of flag

flag = pygame.transform.scale(pygame.image.load('nvren/cccp.png'), (100,50))
pole = pygame.image.load('nvren/pole.png')#flagpole image
flagr = False #boolean for if the flag is raising

w, h = display1.get_size() #width height of window
x = 3
intro()
while(True):
    flagpole = bolin - bob.position +200 #horizontal coordinate of flagpole
    corefont = myfont.render(' ', False, (black))
    font1 = myfont.render(' ', False, (black))
    redraw = True #the labels must be drawn during jumps, this boolean prevents drawing twice
    if(bob.stepsback > 20):
        #checks if player has retreated too many steps
        if bob.move:
            bob.alive = False
            font1 = myfont.render('You have been executed for retreating', False, (black))

    
    
    
    keys = pygame.key.get_pressed() #gets keypressed events
    if(keys[pygame.K_RIGHT] ):
        if(bob.alive):
            #checks if the player is alive
            bob.orientation = 'right'
            tv= -3
            bob.traveled +=1

        else:
            #player is not alive. Tank and other objects should not move.
            tv=0
        b = x % len(bob.player) 
        #This is the variable that loops through the indexes of the player image array
        #x increases indefinitely, however the mod of x is repeating
        ula = False #this boolean checks if the flag has been successfully raised to the top of pole
        #this boolean is set to false here because the victory message should disappear after moving player
    elif(keys[pygame.K_LEFT] ):
        if(bob.alive) :   
            #checks for player alive
            bob.orientation= 'left'
            tv=3
            bob.stepsback += 1

        else:
            tv=0 #keeps tank stationary
        b = x % len(bob.player)
        ula = False
        #same logic as above
    else:
        b = 0
        tv = 0
    
    display1.fill(white)
    if(position[0]<-1000):
        #checks if the tank is off the left side of the screen
        if(spawntank):
            #if more tanks are desired, the image of tank is moved to the original position to the right of screen
            position=[1400, 300]

    position = [position[0]+tv, position[1]] #if l/r buttons pressed, tank will move
    display1.blit(tank, position)
    
    
    if(keys[pygame.K_a]):
        #increases the speed that everything moves
        sprint = 0.05
    else:
        sprint = 1
        
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_k:
                #kill command
                bob.alive = False
            if event.key == pygame.K_SPACE:
                #jumping
                while (not height == 0):
                    #important elements are redrawn here as it is a nested loop and thus anything drawn outside 
                    #of this loop temporarily will not show
                    #player[2] is chosen as jump image because it resembles jumping
                    display1.fill(white)
                    display1.blit(tank, position)
                    if (bob.orientation == 'right'):    
                        display1.blit(bob.player[b], (200, height))
                    if (bob.orientation == 'left'):
                        display1.blit(pygame.transform.flip(bob.leftplayer[b], True, False), (200, height)) 
                    height += -10
                    pygame.display.update()
                jump = True
           
            if bob.position >bolin - 200:
                #checks if player is near flagpole
                if event.key == pygame.K_f:
                    #checks for flag raise command
                    flagr = True
                    ula = True
                    
    
    
    
    if bob.position> bolin - 1400:
        #draws flagpole when player is close enough so that it should be on the screen
        display1.blit(pole, (flagpole, 400))
    
    if bob.orientation == 'right':
        if not(bob.alive):
            display1.blit(bob.dead, (0, 450))
        
        elif(height == 200):
            display1.blit(bob.player[b], (200, 200))
           
        
            
        if(not height == 200):
            #checks if the player has jumped and now needs to fall down slowly
            jump = False
            display1.fill(white)
            display1.blit(tank, position)
            display1.blit(pole, (flagpole, 400))
            scorefont = myfont.render('Dist: %d'%(bob.position), False, (black))
            display1.blit(scorefont, (20,20))
            label = myfont.render('<-- Moscow     Berlin -->', False, (black))
            display1.blit(label, (470, 20))
            display1.blit(bob.player[1], (200, height))
            height +=10
            redraw= False
            pygame.display.update()
            
    elif bob.orientation == 'left':
        if not bob.alive:
            display1.blit(pygame.transform.flip(bob.dead, True, False), (200, 450))
        
        elif(height == 200):

            display1.blit(pygame.transform.flip(bob.player[b], True, False), (200, 200))
        if(not height == 200):
            display1.fill(white)
            display1.blit(tank, position)
            display1.blit(pole, (flagpole, 400))
            scorefont = myfont.render('Dist: %d'%(bob.position), False, (black))
            display1.blit(scorefont, (20,20))
            label = myfont.render('<-- Moscow     Berlin -->', False, (black))
            display1.blit(label, (470, 20))
            display1.blit(pygame.transform.flip(bob.leftplayer[1], True, False), (200, height))
            height +=10
            redraw = False
            pygame.display.update()
            
    if bob.position > bolin -1000:
        #stops tanks from forming when close to flagpole
        spawntank = False

    if bob.position >bolin - 200:
        corefont = myfont.render('press f to raise flag', False, (black))
    
    if flagr:
        if not p == 400:
            #if flag is not at the desired final height
            display1.blit(flag, (flagpole+20, p))
            p+=-1
            ula = True
        else:
            #if flag is at final height
            display1.blit(flag, (flagpole+20, 400))
            if ula:
                #prints victory message
                font1 = myfont.render('                 ULA!!! ULA!!!', False, (black))
        corefont = myfont.render(' ', False, (black))#removes the press f for raise flag message
        
        bob.move = False


    display1.blit(corefont, (400, 500))

    
    x+=1 #increments x variable, this is useful for cycling through player[]
    bob.position = bob.traveled - bob.stepsback
    if redraw:
        scorefont = myfont.render('Dist: %d'%(bob.position), False, (black))
        display1.blit(scorefont, (20,20))
        label = myfont.render('<-- Moscow     Berlin -->', False, (black))
        display1.blit(label, (470, 20))
    display1.blit(font1, (70, 300))

    
    pygame.display.update()
    time.sleep(0.08*sprint)
    #the images cycle through too fast, this sleep ensures a smooth animation
    #animation is speeded up 
    




