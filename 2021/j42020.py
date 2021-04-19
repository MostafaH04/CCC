a = input()

num = []

for i in range(len(a)):
  if a[i] == "L":
    num.append(1)
  elif a[i] == "M":
    num.append(2)
  elif a[i] == "S":
    num.append(3)

numCount= 0

for i in range(len(num)-1):
  minLoc = i
  for j in range(i+1 , len(num)):
    if num[j] < num[minLoc]:
      minLoc = j
  x = num[minLoc]
  num[minLoc] = num[i]
  num[i] = x
  if minLoc != i:
    numCount+=1



print(numCount)



