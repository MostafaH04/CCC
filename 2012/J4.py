c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d = []
for i in c:
  d.append(i)

a = int(input())
b = input()
newB = ""
for i in range(len(b)):
  curr = ''
  x = d.index(b[i])
  s = 3*(i+1) + a
  sum = x-s
  curr = d[sum]
  newB += curr

print(newB)
