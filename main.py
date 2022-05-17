import math

input = input()

inputTrim = input.replace(" ", "")

map = map(int, inputTrim)
list = list(map)

n = list[0]
k = list[1]

print(math.comb(n,k))

