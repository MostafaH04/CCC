word = input()
letters = list(word)
count = 0;

for i in letters:
  if i in 'IONSHZXN':
    count += 1

if count == len(word):
  print("YES")
else:
  print("NO")
