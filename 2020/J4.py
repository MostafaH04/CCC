t = input()
s = input()

newS = s
done = False

for i in range(len(s)-1):
  newS = newS[1:]
  newS += s[i]
  if newS in t or s in t:
    print("yes")
    done = True
    break

if not done:
  print("no")