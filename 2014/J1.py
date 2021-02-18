a = int(input())
b = int(input())
c = int(input())

type = ["Equilateral", "Isosceles", "Scalene", "Error"]

if a == b and b == c and c == 60:
  print(type[0])
elif (a == b or b == c or c == a) and a + b + c == 180:
  print(type[1])
elif a + b + c == 180 and a != b and b != c and c != a:
  print(type[2])
elif a + b + c != 180:
  print(type[3])