a = int(input())
b = int(input())
c = int(input())

import math

if c == 1:
  print(int(a/b))
else:
  print(int(math.log(((a * (c-1))/b)+1)/math.log(c)))
