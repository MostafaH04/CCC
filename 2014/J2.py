useless = input()

votes = input()

aVotes = 0
bVotes = 0

for i in votes:
  if i == "A":
    aVotes += 1
  elif i == "B":
    bVotes +=1

if aVotes > bVotes:
  print('A')
elif bVotes > aVotes:
  print('B')
else:
  print("Tie")
