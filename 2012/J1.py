a = int(input())
b = int(input())

if b <= a:
  print("Congratulations, you are within the speed limit!")
elif b > a and b <= a +20:
  print("You are speeding and your fine is $100.")
elif b > a+20 and b <= a+30:
  print("You are speeding and your fine is $270.")
elif b > a + 30:
  print ("You are speeding and your fine is $500.")
