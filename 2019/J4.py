a = [[1,2],[3,4]]
aCopy = a

bInput = []
b = input()
for i in b:
  bInput.append(i)
for i in bInput:
  if i == 'H':
    aCopy.reverse()
  elif i == 'V':
    aCopy[0].reverse()

    aCopy[1].reverse()

for i in aCopy:
  print(str(i[0])+" "+str(i[1]))
