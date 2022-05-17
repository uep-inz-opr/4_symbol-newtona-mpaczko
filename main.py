import math
from re import S

input = input()

inputTrim = input.replace(" ", "")

map = map(int, inputTrim)
list = list(map)

x = list[0]
y = list[1]

if y == x:
    print(1)
elif y == 1:         # see georg's comment
    print(x)
elif y > x:          # will be executed only if y != 1 and y != x
    print(0)
else:                # will be executed only if y != 1 and y != x and x <= y
    a = math.factorial(x)
    b = math.factorial(y)
    c = math.factorial(x-y)  # that appears to be useful to get the correct result
    div = a // (b * c)
    print(div) 


