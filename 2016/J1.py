types = ['1','2','3','-1']

wins = 0
losses = 0

for i in range(1,7):
  a = input()
  if a == 'W':
    wins += 1
  elif a == 'L':
    losses += 1

if wins >= 5:
  print(types[0])
elif wins >= 3:
  print(types[1])
elif wins >= 1:
  print(types[2])
else:
  print(types[3])
