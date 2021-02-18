N = int(input())

scores = []

for i in range(2):
  scores.append(input().split())


answered = False
days = 0
swiftSum = 0
semaSum = 0
for i in range(N): 
  swiftSum += int(scores[0][i])
  semaSum += int(scores[1][i])

  if semaSum == swiftSum:
    days = i + 1
  
print(days)