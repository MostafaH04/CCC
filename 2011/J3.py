a = int(input())
b = int(input())

stuff = [a,b]
while True:
  sum = stuff[-2] - stuff[-1]
  stuff.append(sum)
  if stuff[-1]>stuff[-2]:
    break

print(len(stuff))
