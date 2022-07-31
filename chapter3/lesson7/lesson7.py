import math

num = [0.0, 1, 3.0, 4, 4.2, 5.1, 7, 8.9, 9.0 ]

a = []
for x in num:
  if type(x) == int:
    a = [*a, math.pow(x, 2)]

print(a)
