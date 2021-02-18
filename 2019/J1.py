#team 1 scores
a1 = int(input())
a2 = int(input())
a3 = int(input())

#team 2 scores
b1 = int(input())
b2 = int(input())
b3 = int(input())

# a team score
aScore = a1 * 3 + a2 * 2 + a3 

#b team score
bScore = b1 * 3 + b2 * 2 + b3

if aScore > bScore:
  print("A")
elif bScore > aScore:
  print("B")
else:
  print("T")
