directions = []

while True:
  a = input()
  direct = ''
  if a == '99999':
    break
  if (int(a[0])+int(a[1]))%2 == 0:
    if int(a[0])+int(a[1]) != 0:
      direct = "right"
      directions.append(direct)
    else:
      direct = directions[-1]
      directions.append(direct)
  elif (int(a[0])+int(a[1]))%2 != 0:
    direct = "left"
    directions.append(direct)
  
  print(direct+" "+a[2:])


  3:31 PM 2/17/2021