import os

def gethighscores():
    def getlast(element):
        '''gets last element of array, used for sorting scores'''
        return int(element[-1])
        #make sure to cast to int or else 90 is before 1000
            
        
    highscores =[] #highscores is array got from save file
    scores =[] #scores stores the sorted, fused strings to print
    with open ('highscores.txt', 'r') as file:
        for line in file.readlines():
            try:
                getlast(line.split())
            except:
                continue
            highscores.append(line.split())
    highscores.sort(key = getlast, reverse=True)
    for score in highscores:
        scores.append(' '.join(score))
    if(len(scores)<5):
        for x in range(5-len(scores)):
            scores.append('----')
    return scores

def gethelp():
    os.startfile(os.path.join(os.path.dirname(__file__),'manual.pdf'), 'open')

def addhighscore(name, score):
    with open ('highscores.txt', 'a') as file:
        element = str(name +' '+str(score)+'\n')
        file.write(element)
        
