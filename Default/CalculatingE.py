#this program calculates e to a specified accuracy
# e = (1+1/n)^n, this gets more accurate as n becomes larger
n=1000000.;
#asks user to input an accuracy
accuracy=input('please specify accuracy (whole numbers only): \n');

#declares an exact value of e correct to 150 digits (without the 2. in front)
ee= 718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260

#checks that computer is able to correctly perform calculations
if(1+1 != 2):
    print('computer unable to provide accurate calculation at this time');  

#check that input is valid
elif(accuracy.isdigit() and int(accuracy)>0): 
    #establishes a value of n; a larger accuracy requires larger n      
    n=n+1000.*int(accuracy);
    e=(1+1/n)**n;
    if(e!=1.0):
        print('e = %f'%e);
    else:
        print('insufficient memory for such accuracy')
    

elif(accuracy.__eq__('exact')):
    print('e = 2.%s'%(ee))
    

#if user inputs unacceptable value
else:
    print('illegal input');


