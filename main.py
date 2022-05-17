import math

input = input()

inputTrim = input.split()

map = map(int, inputTrim)
list = list(map)


x = list[0]
y = list[1]


print(math.comb(x, y))

