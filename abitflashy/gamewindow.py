import pygame
from numpy.random.mtrand import randint
import sys
from sympy.sets.sets import Interval, Intersection
from abitflashy.filewrite import gethighscore, savehighscore



def intro():
    #this is the opening page of the game
    if(firsttime):
    #detects if it is first time running program, determines whether or not to show intro screen
        
        while(True):
            
            display1.fill((0,0,0))
            
            #text that will go on the intro screen
            introfont = myfont.render('A BIT FLASHY', False, (255,255,255))
            introfont2 = myfont.render('press space to start', False, (255,255,255))
            warning = warningfont.render('WARNING: this game contains flashing colors.', False, (255,0,0))
            warning2 =warningfont.render('Do not play if you suffer from seizures.', False, (255,0,0))
           
            #detects for user input from keyboard
            for introevent in pygame.event.get():
                if(introevent.type == pygame.KEYDOWN):
                    if(introevent.key==pygame.K_SPACE):
                        return 
                        #this makes the code go out of the function and continue with the rest of the program
                    if(introevent.key == pygame.K_ESCAPE):
                        sys.exit()
           
            #draws all the text onto the screen
            display1.blit(introfont, ( 400,100 ))
            display1.blit(introfont2, (250,300 ))
            display1.blit(warning, (100, 500))
            display1.blit(warning2, (100, 550))
            
            pygame.display.update()
                

        
def run():
    
    #sets useful variables and gets window size
    black = [0,0,0] 
    w, h = display1.get_size()
    
    pygame.mouse.set_visible(False) #hides the mouse for the game
    
    
    x = int(w/2)
    y =int(h/2)+200
    # x, y refer to pygame coordinates of player
    
    score =0
    
    flagy = -263
    flagx = randint(0,scr_width-500)
    #pygame coordinates of the obstacle, the x value is randomly generated
    
    intro()
    #introduction screen displayed if it is firsttime is true
    
    pygame.mixer.music.play(-1)
    #plays the background music during gameplay
    
        
    while(True):
        scorefont = myfont.render('Score: %d'%score, False, (0,0,0))
        #text that shows current score in upper left corner
        
        if(flagy > scr_height+270):
            #detects for an obstacle successfully avoided (off the bottom of screen)
            flagy = - 270
            flagx = randint(0,scr_width-500)
            #obstacle moved to new position above player, with random x value
            
            score += 1
        
        
        color = [randint(0,255),randint(0,255),randint(0,255)]
        #randomly generates a color for the background
        
        flagy = flagy +12
        #this is the speed that the obstacle falls down
        
        #detects for user input from keyboard (escape button only)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT): 
                sys.exit()
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    sys.exit()
               
        
        #detects user controlling player (this method must be used or else 
        #holding a button only renders one click, and the player will not 
        #continuously move. It is also checked that the player will not go 
        #off the screen after moving
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_RIGHT]):
            if(x+10 in range(0,scr_width-121)):
                x = x+10
        if(keys[pygame.K_LEFT]):
            if (x-10 in range(0, scr_width)):
                x = x-10
        
        if(not Intersection(Interval(y, y+140), Interval(flagy, flagy+150)).is_EmptySet):
            #checks if the intervals of y coordinates of the obstacle and player overlap
            
            if (not Intersection(Interval(x, x+121), Interval(flagx, flagx +500)).is_EmptySet):
            #given that the y coordinates overlap, check if the x coordinates overlap
                
                display1.fill(black) 
                
                global highscore #defined global because variable is in function
                
                if(score>highscore):
                    #check if score this round is higher than highscore, update highscore if needed
                    highscore = score
                    savehighscore(highscore) 
                    
                #this is the text on the death screen         
                text = myfont.render('you have died.', False, (255,255,255))
                scoretext = myfont.render('Score: %d   Highscore: %d'%(score, highscore), False, (255,255,255))
                text2 = myfont.render('press space to restart', False, (255,255,255))
                
                while(True):
                    
                    #while on death screen, checks for user input
                    for event in pygame.event.get():
                        if(event.type == pygame.QUIT): 
                            sys.exit()
                        elif(event.type == pygame.KEYDOWN):
                            if(event.key == pygame.K_ESCAPE):
                                sys.exit()
                            if(event.key== pygame.K_SPACE):
                                #restart the game
                                global firsttime
                                pygame.mixer.music.stop()
                                #stops music so it can be replayed
                                
                                firsttime = False
                                #prevents the intro screen from showing
                                
                                run()
                                
                    #draws the text onto death screen        
                    display1.blit(text, (int(scr_width/2)-500,200))
                    display1.blit(scoretext, (int(scr_width/2)-500, 300))
                    display1.blit(text2, (int(scr_width/2)-500, 400))
                    pygame.display.update()
                    
        
        #clears game window, moves all objects, and redraws them. Also draws on score.
        display1.fill(color)
        display1.blit(player, (x,y))
        display1.blit(flag, (flagx,flagy))
        display1.blit(scorefont, (40, 50))
        
        pygame.display.update()


#initializes pygame and pygame font
pygame.init()
pygame.font.init()  

#defines fonts that are needed
myfont = pygame.font.SysFont('Comic Sans MS', 80)
warningfont = pygame.font.SysFont('Comic Sans MS', 50)

#gets the highscore from previous rounds
try:    
    highscore = gethighscore()
except:
    #in case unable to get highscore from save
    highscore = 0
 
#defines the window and the firsttime variable
scr_width, scr_height = pygame.display.Info().current_w, pygame.display.Info().current_h
display1 = pygame.display.set_mode((scr_width,scr_height), pygame.FULLSCREEN)
firsttime = True  

#loads necessary files NOTE: will give libpng sRGB warning. This is due to using Photoshop
#RGB pictures. This has no effect on program.
pygame.mixer.music.load('music.wav')
player = pygame.image.load('player.png')
flag = pygame.image.load('log.png')

#executes the game
run()

