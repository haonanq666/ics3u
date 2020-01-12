import pygame
import sys
from rst import input
import pygbutton
import random
from rst.projmotion import railgun, target, nontarget
import time as t
from math import tan, pi
from rst.read import gethighscores, addhighscore, gethelp

pygame.init()
pygame.font.init()  

black = (0,0,0)
white = (255,255,255)
green = (0, 255, 0)

scr_width, scr_height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((scr_width,scr_height), pygame.FULLSCREEN)

def intro():
    '''first screen that shows up to user; accepts a player name and selects a character'''
    global playername
    try:
        #if firsttime play, playername not defined and thus text box should be empty
        textinput= input.TextInput(initial_string=playername)
    except:
        textinput = input.TextInput()
        pygame.mixer.music.pause() #only stop if it is the first time intro screen

    
    position = [500, 500]
    #position of text box, all other elements adjusts to this position.
    
    bigfont = pygame.font.SysFont('Comic Sans MS', 80)
    smallfont = pygame.font.SysFont('Comic Sans MS', 30)
    
    prompt = smallfont.render('enter name and select character to begin', True, (black))
    title = bigfont.render('PROJECT-RAILGUN', False, (black))

    paojie = pygbutton.PygButton((500, position[1]+160, 120, 30), 'Misaka Mikoto')#button to select misaka
    railgun = pygbutton.PygButton((650, position[1]+160, 120, 30), 'Railgun')#button to select a railgun
    help = pygbutton.PygButton((10, 10, 120, 30), 'Help')
    
    paojieicon = pygame.image.load('images/misakaicon.png')
    railgunicon = pygame.image.load('images/railgunicon.jpeg')
    #these are icons that help player choose
    
    
    while(True):
        screen.fill(white) #clear screen
        events = pygame.event.get()
        
        for event in events:
            if 'click' in paojie.handleEvent(event) and (not textinput.get_text().isspace()) and ( textinput.get_text()):
                #checks for button clicked
                playername = textinput.get_text()
                playerchar = 'misaka'
                #sets player's name and the character they chose
                pygame.mixer.music.unpause()

                main(playerchar)
            if 'click' in railgun.handleEvent(event) and (not textinput.get_text().isspace()) and ( textinput.get_text()):
                playername = textinput.get_text()
                playerchar = 'railgun'
                pygame.mixer.music.unpause()

                main(playerchar)
            if 'click'  in help.handleEvent(event):
                pygame.display.iconify()
                gethelp()
    
            if event.type == pygame.QUIT:
                exit()
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    sys.exit()
                
        
        textinput.update(events) #this updates the text inside text input box
        screen.blit(textinput.get_surface(), position)
        #this is the text input surface
        
        pygame.draw.rect(screen ,(0,0,0),(position[0]-2, position[1]-2,270,35), 3)
        #this is the border of the textbox
        
        paojie.draw(screen)
        railgun.draw(screen)
        help.draw(screen)
        screen.blit(pygame.transform.scale(paojieicon, (100, 100)), (510, position[1]+50))
        screen.blit(pygame.transform.scale(railgunicon, (100, 100)), (660, position[1]+50))
        screen.blit(prompt, (position[0]-100, position[1]-60))
        screen.blit(title, (300, 200))
        #drawing all the elements onto screen

        pygame.display.update()

def ending(condition):
    '''ending of the game, allows for quit or restart, displays highscores'''
    smallfont = pygame.font.SysFont('Comic Sans MS', 60)
    if condition =='destroyedgreenhouse':
        deathmsg = smallfont.render('you destroyed a non-target!    Score: %d'%score, False, black)
    elif condition =='outofammo':
        deathmsg = smallfont.render('you ran out of ammo!               Score: %d'%score, False, black)
    #different death message based on how the player lost
    
    addhighscore(playername, score)
    #first add current high score so that if it is top five it will be displayed
    highscores = gethighscores()
    
    restart = pygbutton.PygButton((850, 300, 300, 100), 'Restart')
    quit = pygbutton.PygButton((850, 500, 300, 100), 'Quit')
    
    score999 = smallfont.render('Highscores:', False, green)# the title "Highscores:"
    score0 = smallfont.render('1 '+highscores[0], False, green)
    score1 = smallfont.render('2 ' +highscores[1], False, green)
    score2 = smallfont.render('3 '+highscores[2], False, green)
    score3 = smallfont.render('4 '+highscores[3], False, green)
    score4 = smallfont.render('5 '+highscores[4], False, green)
    #the top five highscores
    while(True):
        screen.fill((255,255,255))
        events = pygame.event.get()
        
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if 'click' in restart.handleEvent(event):
                reset()#reset the values for score and shots
                intro()
            if 'click' in quit.handleEvent(event):
                sys.exit()
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    sys.exit()
              
                
        screen.blit(deathmsg, (30, 60))
        
        restart.draw(screen)
        quit.draw(screen)
        
        screen.blit(score999, (50, 180))
        screen.blit(score0, (80, 280))
        screen.blit(score1, (80, 360))
        screen.blit(score2, (80, 440))
        screen.blit(score3, (80, 520))
        screen.blit(score4, (80, 600))
        #draw everything
        
        pygame.display.update()
        

def main(type):
    def getvertpos(point, angle):
        '''returns the x and y pygame coordinates given its x position'''
        if xposition<550:
            x=xposition
            y = 768-(xposition*tan(angle*(pi/180))-tan(angle*(pi/180))*(initpos)+initialheight)
            #y - y= m(x-x) y= mx -mx+y
            #position, 368
        elif 549<xposition<1000:
            y=-100
            x= 600 
        else:
            y=768-((xposition*tan(angle*(pi/180)))-tan(angle*(pi/180))*(point[0])+point[1])
            x = xposition - 400
        return [x, y]
            
    def getgreenpos():
        '''returns array that contains two random numbers that are spaced apart from redhouse position and each other'''
        pos = random.randint(600, 1366-50)
        pos2 = random.randint(600, 1366-50)
        if redhouseposition-50<pos <redhouseposition+50:
            return getgreenpos()
        elif redhouseposition -50 <pos2< redhouseposition +50:
            return getgreenpos()
        elif pos -50 < pos2< pos +50:
            return getgreenpos()
        else:
            return [pos, pos2]
    def checklost():
        '''checks if the game lost conditions are met, returns boolean'''
        if greenhouse1.isdestroyed(projrect):
            return True
        elif greenhouse2.isdestroyed(projrect):
            return True
        else:
            return False
    
    def checkammo():
        '''checks if ammo is out, ending called if true'''
        #this must be done separate when not firing so that the last shot can be fired
        if shots <= 0:
            t.sleep(2)
            ending('outofammo')
        
    
    gunangle = 1
    #angle of the gun, can be changed
    
    
    #width of screen is 1366
    position = random.randint(10, 100)
    #position is horizontal position of player
    if(type == 'misaka'):
        gun = pygame.transform.scale(pygame.image.load('images/misaka.png'), (200, int(200/0.7641723356)))
        xposition= position +50
        initpos = xposition
        initialheight = 268
        gunheight = 400
        gunrect = pygame.Rect(0,0,0,0)
    elif(type == 'railgun'):
        gun = pygame.transform.scale(pygame.image.load('images/railgun.png'), (300, int(300*(293/442))))
        
        xposition = position+50
        initpos= xposition
        initialheight = 168
        gunheight = 450
        gunrect = pygame.Rect(position, gunheight, 300, int(300*(293/442)))
    

    player = railgun(position, gun) #creates new railgun instance called player
    proj = pygame.transform.scale(pygame.image.load('images/projectile.png'), (60, 20))
    
    redhouseposition = random.randint(700, 1366-50)# generates random position for redhouse
    
    redhouse = target(redhouseposition)
    greenpos = getgreenpos()
    greenhouse1 = nontarget(greenpos[0])
    greenhouse2 = nontarget(greenpos[1])
    #used function that made sure to space out the houses so they do not overlap
        
    
    destroycounter = False
    destroycount = 0
    #if the green house is destroyed, a delay is invoked before moving on
    
    lostcounter = False
    lostcount = 0
    #if greenhouseis destroyed, a delay is done before moving on
    
    firing = False#whether the railgun is firing
    current = 70000
    
    paused = False
    smallfont = pygame.font.SysFont('Comic Sans MS', 30)
    
    distmark = smallfont.render('<-- 400 m', False, black)
    #small marker showing the distance omitted by the black line

    while(True):
        global shots, score
        screen.fill((0,191,255)) #this is a light blue color
        events = pygame.event.get()
        pygame.draw.rect(screen, (0, 255, 0), (0, 680, 1366, 108 ))#green rectangle representing ground
        
        shotsleft = smallfont.render('Ammo Left: %d' % shots, False, black)
        currentscore = smallfont.render('Score: %d' % score, False, black)
        currentcurrent = smallfont.render('Current: %d A' %current, False, black)
        currentangle = smallfont.render('Angle: %d'%gunangle, False, black)
        pausedtext = smallfont.render('Game Paused', False, black)
        #data for the player to see
        
        for event in events:
           
            if event.type == pygame.QUIT:
                exit()
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    sys.exit()
                if(event.key== pygame.K_SPACE) and not paused:
                    if not firing:
                        #prevents shots from decreasing when space is pressed without firing another projectile
                        shots+= -1
                    firing = True
                if(event.key== pygame.K_p):
                    if paused: 
                        paused = False
                    elif not paused:
                        paused = True
                if(event.key == pygame.K_m):
                    if paused:
                        pygame.display.iconify()
                        
        keys = pygame.key.get_pressed()
        if not firing and not paused:
            checkammo() #if the last ammo is used, it waits to see if it hits before deciding win or lose
            if(keys[pygame.K_RIGHT]):
                if(gunangle-1 in range(1,90)):
                    #prevents angles out of this range, they will cause weird things to the physics engine
                    gunangle+=-1
            if(keys[pygame.K_LEFT]):
                if (gunangle+1 in range(1, 90)):
                    gunangle+=1
            if(keys[pygame.K_UP]):
                current += 10
            if(keys[pygame.K_DOWN] and (current-10>0)):
                current += -10
                
        if (firing):
            projangle = gunangle #defines an angle variable that can be manipulated (gun angle is required to draw the gun, cannot be changed)
            
            if 1000>xposition>600:
                projangle= 0
            elif xposition>999:
                projangle = - gunangle
            projposition = getvertpos([position+player.getrange(current, gunangle), 168], projangle)
            projrect = pygame.Rect(projposition[0]+40,projposition[1], 20,20)
            # projrect only contains the head of the projectile for more realistic collision detection
            if projposition[0]>500:
                if(player.getrange(current, gunangle)<400):
                #if the angle is too low the projectile will not go far, this prevents abnormalities
                    firing = False
                    xposition = position
            if projposition[1] >  660:
                if projposition[0]>600:
                    #if the projectile hits the ground
                    firing = False
                    xposition = position #resets the position of the projectile
                        
            if checklost():
                lostcounter = True
                firing = False
            if redhouse.isdestroyed(projrect) and not lostcounter: #if both red and green house destroyed then game lost
                destroycounter = True
                firing = False
                        
            
            if not projrect.colliderect(gunrect):    
                #if the projectile is inside gun, it does not show
                screen.blit(pygame.transform.rotate(proj, projangle), (getvertpos([position+player.getrange(current, gunangle), 168], projangle)))

            if not paused:
                xposition +=1   
            
        if destroycounter and not paused:
            #starts to increment destroy counter if destroyed house
            destroycount+=1
        if destroycount>60:   
            shots+=2
            score += 1
            main(type)
        
        if lostcounter and not paused:
            lostcount+=1
        if lostcount>80:
            ending('destroyedgreenhouse')
            
        pygame.draw.rect(screen, black, (600, 0, 0, 768), 5)
        screen.blit(pygame.transform.rotate(player.image, gunangle), (position, gunheight))
        screen.blit(redhouse.getimage(), (redhouseposition, 630))
        screen.blit(greenhouse1.getimage(), (greenpos[0], 630))
        screen.blit(greenhouse2.getimage(), (greenpos[1], 630))
        
        
        if paused:
            screen.blit(pausedtext, (620, 400))
        
        screen.blit(distmark, (610, 50))
        
        screen.blit(shotsleft, (40, 120))
        screen.blit(currentscore, (40, 160))
        screen.blit(currentcurrent, (40,40))
        screen.blit(currentangle, (40, 80))
        #draws everything
        pygame.display.update()

 
def reset():
    '''resets certain variables for new game'''
    global score, shots        
    score = 0
    shots = 5
reset()
pygame.mixer.music.load('images/onlymyrailgunxianyaoyiyi.mp3') #load background music
pygame.mixer.music.play(-1)

intro()
