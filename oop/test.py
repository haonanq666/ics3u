from math import cos
class Thing(object):
    def __init__(self):
        self.name 
        self.current
        self.vision

        
    

class World(object):
    def __init__(self, size):
        self.size = size
        self.contents = []
    def addThing(self, element):
        self.contents.append(element)
        element.inworld= True
    def startSimulation(self):
        print(self.contents)
    def timeTravelForTwo(self, era, year, person1, person2):
        self.time = (year,era)
        self.contents.clear()
        self.contents.append(person1)
        self.contents.append(person2)
        
    def unite(self, person1, person2):
        return (person1,person2)
    def lockThing(self, locked):
        locked.inworld = True
        self.escapable = False
    
        


class SineWave(object):
    def getTangent(self, xposition):
        return(cos(xposition))
    
class PointSet(object):
    def getDimensions(self):
        return self.dimensions
class Circle(object):
    def getCircumference(self):
        return 3.141592654
class Sequence(object):
    def setLimit(self, limit):
        self.limit = limit
    def toLimit(self):
        return self.xposition



class Lovable(Thing, SineWave, PointSet, Circle):
    
    def __init__(self, name, dimensions, ishappy, xposition, inworld):
        self.name = name
        self.dimensions = dimensions
        self.ishappy = ishappy
        self.xposition  =  xposition
        self.inworld = inworld
        self.actions = []
        self.feelings = []
    def getXPosition (self):
        return self.xposition
    def addAction(self, actionname, actionposition):
        self.actionname = actionname
        self.actionposition = actionposition
        self.actions.append(actionname)
    def toggleCurrent(self):
        self.current = 'AC'
        self.current = 'DC'
    def canSee(self, cansee):
        self.vision = cansee
    def addFeeling(self, feeling):
        self.feelings.append(feeling)   
    def getNumSimulationsAvailable(self): 
        return self.dimensions*2
    def getNumSimulationsNeeded(self):
        return self.dimensions*1
    def setSatisfaction(self, satisfaction):
        self.satisfaction = satisfaction
    def toSatisfaction(self):
        return self.name+'satisfaction'
    def getFeelingIndex(self, feeling):
        return len(feeling)
    def requestExecution(self, world):
        world.startSimulation(self.dimensions)
    
        
if __name__ == '__main__'  :
    me = Lovable(1,1,1,1,1)
    setattr(me, 'alu','thing')
    
    print(me.alu)
    print(me.getTangent(me.getXPosition()))
    me.addAction('sit', 1.03)
    print(me.actions)
