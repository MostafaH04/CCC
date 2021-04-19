a = int(input())
b = input().split()
c = input().split()

d = []
f = []

for i in b:
  d.append(int(i))
for i in c:
  f.append(int(i))



h = []
for i in range(a):
  h.append([])
  h[i].append(d[i])
  h[i].append(d[i+1])

sum = 0

for i in range(len(h)):
  if h[i][0] != h[i][1]:
    stuff = h[i][0] + h[i][1]
    stuff = stuff/2
    stuff = stuff * f[i]
    
  else:
    stuff = h[i][0]*f[i]
  sum += stuff
  
if sum % 2 == 0:
  print(int(sum))
else:
  print(sum)

