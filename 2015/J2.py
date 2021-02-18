sentence = input()

hCount = sentence.count(":-)")
sCount = sentence.count(":-(")

if hCount > sCount:
  print("happy")
elif sCount > hCount:
  print("sad")
elif sCount == hCount:
  if sCount == 0:
    print("none")
  else:
    print("unsure")
