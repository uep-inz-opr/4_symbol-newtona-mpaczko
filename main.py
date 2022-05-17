import math
from re import S

input = input()

inputTrim = input.replace(" ", "")

map = map(int, inputTrim)
list = list(map)

x = list[0]
y = list[1]

if y == 1 or y == x:
    print(1)

if y > x:
    print(0)        
else:
    a = math.factorial(x)
    b = math.factorial(y)
    div = a // (b*(x-y))
    print(div) 


