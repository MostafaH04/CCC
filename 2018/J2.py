a = int(input())
b = input()
c = input()

count = 0
for i in range(len(b)):
  if b[i] == c[i]:
    if b[i] == 'C':
      count +=1

print(count)