principal=20
days = input('how many days has Vincent not returned money: \n')
print('calculating...'+'.'*85+'|')
for i in range(int(days)-1):
    principal = principal**3
    print(u'\u25A0'*int(100/(int(days)-1)), end="")
if(int(100/(int(days)-1))<100):
    for b in range(100-(int(days)-1)*int(100/(int(days)-1))):
        print(u'\u25A0', end='')    
     
print('\n%d'%principal)

