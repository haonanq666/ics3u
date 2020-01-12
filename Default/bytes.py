#any information (in english) received from files or web is in bytes

stringLatin = 'abcdef'
stringNonLatin = '大家好'

#encode as ascii
stringLatin.encode('ascii')
print(stringLatin)

#throws error as it is non-ascii
#stringNonLatin.encode('ascii')
#print(stringNonLatin)

#encode as utf-8 
stringLatin.encode('utf-8')
print(stringLatin)

stringNonLatin.encode('utf-8')
print(stringNonLatin)



#decode bytes
print(b'ABC'.decode('ascii'))

#decode non latin bytes
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))



