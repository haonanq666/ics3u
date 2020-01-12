def savehighscore(highscore):
    #writes the highscore into save.txt
    with open('save.txt','w') as saveg:
        saveg.write(str(highscore))

def  gethighscore():
    #retrieves highscore from save.txt
    with open('save.txt','rt') as saveg:
        return int(saveg.read())
        #call saveg.read() only once as all calling after the first returns null