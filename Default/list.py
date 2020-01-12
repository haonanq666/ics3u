# using list to store data
alphabet = ['a','b','c','d','e']

# get length of list
print(len(alphabet))

# get element 1
print(alphabet[0])

# get last element
print(alphabet[-1])

# print the entire list
print(alphabet)

# print out of range if used len(alphabet), must -1
print(alphabet[len(alphabet)-1])

# append adds to the end of list
alphabet.append('f')
print(alphabet)

# insert(position, 'element') adds element at specified position
alphabet.insert(2,'1433223')
print(alphabet)

# pop removes an element
alphabet.pop(2)
print(alphabet)

# directly replace element
alphabet[2]='1433223'
print(alphabet)







