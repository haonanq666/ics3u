class player(object):
    #players who play the game of monopoly
    def __init__(self, name, initialmoney):
        self.__name = name
        self.__money = initialmoney
        self.__properties = []
    def paymoney(self, amount):
        self.__money = self.__money - amount
    def addmoney(self, amount):
        self.__money = self.__money + amount
    def getmoney(self):
        return self.__money
    def buyproperty(self, name, value, mortgage):
        self.__properties.append(property(name, value, mortgage))
        self.__properties.sort(key=lambda x: x.getname(), reverse=False)
    def sellproperty(self, name):
        for prop in self.__properties:
            if (prop.getname()== name):
                self.__properties.remove(prop)
        self.__properties.sort(key=lambda x: x.getname(), reverse=False)
    def getvalue(self, name):
        #gets value of property
        for prop in self.__properties:
            if prop.getname() == name:
                return prop.getvalue()
    def checkmoney(self):
        return self.__money
    def checkproperties(self):
        for x in range(len(self.__properties)):
            print(self.__properties[x].gettruename())
    def getname(self):
        return self.__name
    def properties(self):
        return self.__properties
    def hasproperty(self, name):
        for property in self.__properties:
            if property.getname() == name:
                return True
        

class property(object):
    def __init__(self, name, value, mortgage):
        self.__name = name
        self.__truename = name #self.name will be modified with an --m to show mortgage, this is never changed. 
        self.__value = value #this is the value it was first bought from the bank for
        self.__mortgage = int(mortgage)
        self.__isMortgaged = False
        self.__houses = 0
    def getMortgage(self):
        #returns mortgage value of property
        return self.__mortgage
    def addhouse(self, number):
        self.__houses = self.__houses + number
    def sellhouse(self, number):
        self.__houses = self.__houses - number
    def Mortgage(self):
        self.__isMortgaged = True
        self.__name = self.__name + '--M'
    def unMortgage(self):
        self.__isMortgaged = False
        self.__name = self.__truename
    def getname(self):
        #due to a mix up, getname returns truename, and vice versa. This is now difficult to correct. 
        return self.__truename
    def gettruename(self):
        return self.__name
    def getvalue(self):
        return self.__value
        
        
        
         
