from moneycount.count import player
print('hello')

def main(): 
    action = input('')#this is where the players input commands
    action = action.split()
    canbuy = True #checks if a property is allowed to be bought
    syntax = False #checks for syntax errors from the user
    if(len(action)==0):
        #if nothing was inputted
        print('you did not do anything')
        main()
    
    
    if(action[0] == 'set'):
        #set to create new game
        newgame()
        if(action[1] == 'playernum'):
            for x in range(int(action[2])):
                name = input('name of player %d'%(x+1))
                players.append(player(name, 1500))
           
            #######
            #######
            
            main()
    
    if(len(players)>0):
        for playa in players:
            #runs through all players
            if(action[0]== playa.getname()):
                syntax = True
                #checks for various keyword commands
                if (action[1] == 'addmoney'):
                    playa.addmoney(int(action[2]))
                elif(action[1]== 'paymoney'):
                    playa.paymoney(int(action[2]))
                    if (3<len(action)):
                        #optional pay to other player
                        for receiver in players:
                            if(action[3] == receiver.getname()):
                                receiver.addmoney(int(action[2]))
                elif(action[1] == 'balance'):
                    #check balance
                    print(playa.checkmoney())
                elif(action[1]== 'properties'):
                    #check properties
                    for pr in playa.properties():
                        print(pr.gettruename())
                
                elif(action[1] == 'buy'):
                    for p in players:
                        for prod in p.properties():
                            if prod.getname() == action[2]:
                                #checks if the property being bought is already owned by others
                                canbuy = False
                    
                    if(5>len(action)):
                        #if buying from bank
                        if canbuy:
                            playa.buyproperty(action[2], int(action[3]), int(action[3])*0.7)
                            playa.paymoney(int(action[3]))
                        else:
                            print('cannot buy this property already owned.')
                    elif (5<len(action)):
                        #if buying from other player
                        #bob buy boardwalk 300 from steve
                        if(action[4]== 'from'):
                            for seller in players:
                                if (action[5]== seller.getname()):
                                    if seller.hasproperty(action[2]):
                                        #checks if seller has property
                                        seller.addmoney(int(action[3]))
                                        value = seller.getvalue(action[2])
                                        seller.sellproperty(action[2])
                                        playa.buyproperty(action[2], value, value*0.7)
                                        playa.paymoney(int(action[3]))
                                    else:
                                        print(seller.hasproperty(action[2]))
                                        print('cannot buy.')
                elif(action[1]== 'mortgage'):
                    for pro in playa.properties():
                        if pro.getname() == action[2]:
                            pro.Mortgage()
                            playa.addmoney(pro.getMortgage())
                elif(action[1]== 'unmortgage'):
                    for pro in playa.properties():
                        if pro.getname() == action[2]:
                            pro.unMortgage()
                            playa.paymoney((pro.getMortgage())*1.1)
                else:
                    syntax = False
            
        if syntax == False:
            print('illegal syntax')
        
    elif(len(players)==0):
        print('no players')
    
 
    
    main()
    #recursive calling so that program runs again
        
    
def newgame():
    global players
    players = []
newgame()
try:
    #handles errors
    main()
    
except ValueError:
    print('please input correct number')
    main()
except:
    print('improper input')
    main()
    