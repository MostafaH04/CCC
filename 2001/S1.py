thing = input()

def pointTing(list):
  points = 0
  if len(list) == 0:
    points += 3
  elif len(list) == 1:
    points +=2
  elif len(list) == 2:
    points +=1
  for i in list:
    if i == 'A':
      points +=4
    elif i == 'K':
      points += 3
    elif i == 'Q':
      points += 2
    elif i == 'J':
      points += 1
  return points
    

print("Cards Dealt  Points")
clubs = thing[1:thing.index('D')]
Diamonds = thing[thing.index('D')+1:thing.index('H')]
Hearts = thing[thing.index('H')+1:thing.index('S')]
Spades = thing[thing.index('S')+1:]

points = [pointTing(clubs), pointTing(Diamonds), pointTing(Hearts), pointTing(Spades)]

print("Clubs " + " ".join(str(clubs)) + ' '+ str(points[0]))
print("Diamonds " + " ".join(str(Diamonds)) + ' '+ str(points[1]))
print("Hearts " + " ".join(str(Hearts)) +' '+ str(points[2]))
print("Spades " + " ".join(str(Spades)) + ' '+ str(points[3]))

totalTing = 0
for i in points:
  totalTing += i

print("            Total "+ str(totalTing))
