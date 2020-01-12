# -*- coding: utf-8 -*-

#using len() to get length of string

#when len(bytes) is used, number of bytes is returned
print(len('中文'.encode('utf-8')))
print(len(b'abcdef'))

#number of char in str
print(len('abcd'))

#it takes more bytes to code non latin characters; but each char is a char
print(len('你好世界'))

string= input('please input string: \n')
print(len(string))