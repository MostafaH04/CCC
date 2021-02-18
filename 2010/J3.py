on = True
stuff = []
a = 0
b = 0

x = 0
while on:
  stuff = input().split(" ")
  if len(stuff) > 2:
    if stuff[2] == "A":
      stuff[2] = a
    elif stuff[2] == "B":
      stuff[2] = b
  if stuff[0] != '7':
    if stuff[1] == 'A':
      x = a
    elif stuff[1] == 'B':
      x = b
    if stuff[0] == '1':
      x = int(stuff[2])
    elif stuff[0] == '2':
      print(x)
    elif stuff[0] == '3':
      x = x + int(stuff[2])
    elif stuff[0] == '4':
      x = x * int(stuff[2])
    elif stuff[0] == '5':
      x = x - int(stuff[2])
    elif stuff[0] == '6':
      x = x // int(stuff[2])
    if stuff[1] == 'A':
      a = x
    elif stuff[1] == 'B':
      b = x
  else:
    break
