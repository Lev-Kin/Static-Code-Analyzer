import math

x, y = map(float, input().split(' '))

result = math.copysign(abs(x), y)
print(result)