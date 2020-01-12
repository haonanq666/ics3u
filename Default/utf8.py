#changed encoding from GBK to UTF-8 to enable non-latin characters within code
from asyncio.tasks import sleep
print('你好 世界')

#attempt to use ord() and chr()
order = input('please input char: ')
print(ord(order))

character = input('please input character code: ')
print(chr(int(character)))