#using placeholders to format string

name = input('input your name: \n')
age = input('input your age (number only): \n')

#format variables into output
print('your name is %s, your age is %d'%(name, int(age)))

#use %% to represent % when "%" is required 
print('%d %%'%(23))