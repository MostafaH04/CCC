a = int(input())
b = []
c = []
for i in range(a):
  b.append(input())
  c.append(int(input()))

possible = []
current = 0
for i in range(len(c)):
  if c[i] >= current:
    current = c[i]

for i in range(len(b)):
  if c[i] == current:
    possible.append(b[i])

print(possible[0])
