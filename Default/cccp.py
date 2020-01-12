  
from random import randint
from pygame import display, init, FULLSCREEN, mixer, image, event, QUIT, KEYDOWN, K_RIGHTBRACKET, K_f, mouse
import os
import sys
from pygame.constants import K_RIGHT
  
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
  
    return os.path.join(base_path, relative_path)
  
init()
sw, sh = display.Info().current_w, display.Info().current_h
iconi = image.load(resource_path('falg.png'))
display1 = display.set_mode((sw,sh), FULLSCREEN)
white = [255,255,255]  
black = [0,0,0] 
mouse.set_visible(False)
display.set_caption('CCCP -- USSR')
display1.fill(white)
mixer.music.load(resource_path('anthemstalin.wav'))
player = image.load(resource_path('stalin.JPEG'))
x = 0
y =0
a=1
b=1
display.update()
mixer.music.play(-1)
  
while(True):
    display.set_icon(iconi)
    w, h = display1.get_size()
    color = [randint(0,255),randint(0,255),randint(0,255)]
    x = x+a
    y=y+b
    if(x>w-121):
        a = -1
    if(y>h-140):
        b = -1
    if(x<0):
        a=1
    if(y<0):
        b=1
    for even in event.get():
        display.update()
        if(even.type == QUIT): 
            sys.exit()
        elif(even.type == KEYDOWN):
            if(even.key== K_RIGHTBRACKET):
                display.set_mode((600,400))
            if(even.key == K_f):
                display.set_mode((sw,sh), FULLSCREEN)
              
    display1.fill(color)
    display1.blit(player, (x,y))
    display.update()
      
      
          
  
  
  


