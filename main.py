import math

input = input()

inputTrim = input.replace(" ", "")

map = map(int, inputTrim)
list = list(map)

n = list[0]
k = list[1]

if ((n == 0) and (k == 0)):
    print(0)
else:
    print(math.comb(n,k))

