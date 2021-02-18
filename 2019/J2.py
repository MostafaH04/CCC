waw = int(input())
answers = []
for i in range(waw):
  answers.append(input().split())

for i in answers:
  ans = ''
  for x in range(int(i[0])):
    ans += i[1]
  print(ans)
