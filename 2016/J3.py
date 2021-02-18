thing = input()

list = []

for x in range(0, len(thing)):
  for i in range(len(thing)):
    if x == 0:
      current = thing[i:]
    else:
      current = thing[i:-x]
    if current == current[::-1]:
      list.append(len(current))

list.sort()
print(list[-1])