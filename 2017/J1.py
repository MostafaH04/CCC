output = ['1', '2', '3', '4']

x = int(input())
y = int(input())

if x > 0:
  if y > 0:
    print(output[0])
  else:
    print(output[3])
else:
  if y > 0:
    print(output[1])
  else:
    print(output[2])
