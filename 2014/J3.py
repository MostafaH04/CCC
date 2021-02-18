Antonia = 100
David = 100

roundNumber = int(input())

outcome = []

for i in range(roundNumber):
  outcome.append(input().split())

for i in outcome:
  if int(i[0]) > int(i[1]):
    David -= int(i[0])
  elif int(i[0]) < int(i[1]):
    Antonia -= int(i[1])
  
print(Antonia)
print(David)