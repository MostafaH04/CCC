n = int(input())

count = 0

listDiff = []

for i in range(10):
  diff = n - i
  if diff > 0 and (diff < 6 and i < 6 and i not in listDiff):
    listDiff.append(diff)
    count += 1

print(count)