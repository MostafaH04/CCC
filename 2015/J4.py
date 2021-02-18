a = int(input())

b = []
for i in range(a):
  b.append(input().split())

numbers = []
readtime = []

for i in b:
  if int(i[1]) not in numbers and i[0] != "W":
    numbers.append(int(i[1]))
    readtime.append([[],[]])

numbers.sort()

count = 0
for i in b:
  

  if i[0] == "R":
    for k in range(len(numbers)):
      if numbers[k] == int(i[1]):
        readtime[k][0].append(str(count))
  elif i[0] == "S":
    for k in range(len(numbers)):
      if numbers[k] == int(i[1]):
        readtime[k][1].append(str(count))
  
  if i[0] == "W":
    count += int(i[1]) - 1
  else:
    count +=1

for i in range(len(numbers)):
  line = str(numbers[i]) + " " 
  response = 0
  if len(readtime[i][1]) == len(readtime[i][0]):
    for j in range(len(readtime[i][1])):
      response += int(readtime[i][1][j])- int(readtime[i][0][j])
      
  if response == 0:
    response = -1
  
  line += str(response)
  print(line)