a = int(input())
b = int(input())

c = []
for i in range(a):
  c.append([])
  for j in range(b):
    c[i].append('B')

count = 0

d = int(input())
for i in range(d):
  k = input().split()
  k[1] = int(k[1]) - 1
  if k[0] == 'R':
    for i in range(len(c[k[1]])):
      if c[k[1]][i] == 'B':
        c[k[1]][i] = 'G'
        count += 1
      else:
        c[k[1]][i] = 'B'
        count -=1

  elif k[0] == 'C':
    for i in range(len(c)):
      if c[i][k[1]] == 'B':
        c[i][k[1]] = 'G'
        count += 1
      else:
        c[i][k[1]] = 'B'
        count -=1

print(count)


