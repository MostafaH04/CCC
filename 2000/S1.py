machine1 = int(input())
pay1 = [machine1, 30, 35]
machine2 = int(input())
pay2 = [machine2, 60, 100]
machine3 = int(input())
pay3 = [machine3, 9, 10]

pay = [pay1,pay2,pay3]

count = 0

while money > 0:
  #Playing machine 1
  count +=1
  pay[0][0] += 1
  if pay[0][0] == pay[0][2]:
    money += pay[0][1]
    pay[0][0] = 0

  money -= 1

  #playinh machine 2
  if money > 0:
    count +=1
    pay[1][0] += 1
    if pay[1][0] == pay[1][2]:
      money += pay[1][1]
      pay[1][0] = 0

    money -= 1



  #playing machine 3
  if money > 0:
    count +=1
    pay[2][0] += 1
    if pay[2][0] == pay[2][2]:
      money += pay[2][1]
      pay[2][0] = 0

    money -= 1
    


print('Martha plays ' + str(count)+ ' times before going broke.')
