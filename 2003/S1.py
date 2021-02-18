gameOver = False
answer = []
place = 1;
while gameOver == False:
  ting = int(input())
  if ting == 0:
    answer.append('You Quit!')
    gameOver == True
    break
  place += ting
  if place == 9:
    place = 34
  elif place == 40:
    place = 64
  elif place == 67:
    place = 86
  elif place == 54:
    place = 19
  elif place == 90:
    place = 48
  elif place == 99:
    place = 77
  if place > 100:
    place-=ting
  if place == 100:
    answer.append('You are now on square 100')
    answer.append("You Win!")
    gameOver == True
    break
  else:
    answer.append('You are now on square '+str(place))

for i in answer:
  print(i)
