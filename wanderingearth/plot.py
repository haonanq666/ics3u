from matplotlib.pyplot import plot, show
from wanderingearth.ins import updateposition, absposition
from wanderingearth.wanderfunctions import planets, orbrad
import mpmath as mp



x= 0
y=1
screenheight = 768
screenwidth = 1366
scale = ((screenheight-30)/2)/orbrad['pluto']
scalematrix = mp.matrix([[scale,0],
                         [0,    scale]])
 
 
 
def scaletowindow(pointoriginal):
 
    point = scalematrix*pointoriginal
    windowx = point[x] + screenwidth/2 
    windowy = screenheight/2 - point[y]
    return mp.matrix([[windowx],
                      [windowy]])
 
 
quan = 1
num = 200
i = 0
xs =[]
ys = []

while (i<num):
    earth = updateposition()
    for planet in planets:
        px = [scaletowindow(absposition(planet))]
        py = [scaletowindow(absposition(planet))]
    


#xs= [scaletowindow(updateposition())[0] for x in range(num) ]
#ys=[scaletowindow(updateposition())[1] for x in range(num) ]

#plot(xs, ys)

#show()

