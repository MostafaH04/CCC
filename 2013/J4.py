a = int(input())
b = int(input())

c = []

for i in range(b):
  c.append(int(input()))
c.sort()

count = 0

for i in c:
  if i <= a:
    count +=1
    a -= i
  else:
    break

print(count)
