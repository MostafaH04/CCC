n = int(input())
for i in range(n):
  x = input()
  count = 1
  current = ''
  line = ''
  for j in range(1,len(x)):
    if x[j] == x[j-1]:
      count += 1
      current = x[j]
    elif count == 1:
      line += str(count) + " " + x[j-1] + " "
      count = 1
      current = ''
    else:
      line += str(count) + " " + current + " "
      count = 1
      current = ''
  line += str(count) + " " + x[j] + " "
  print(line)
