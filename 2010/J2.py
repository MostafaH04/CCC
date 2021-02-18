e = int(input())
f = int(input())
c = int(input())
d = int(input())
s = int(input())

l = 0
n = 0

def distance(a,b,s):
  person = 0
  while s != 0:
    if s > a and s!=0:
      person += a
      s -= a
    else:
      person +=s
      s-=s
    if s > b and s!=0:
      person -=b
      s -=b
    else:
      person -= s
      s -= s
  return(person)

if distance(e,f,s) > distance(c,d,s):
  print("Nikky")
elif distance(e,f,s) == distance(c,d,s):
  print("Tied")
else:
  print("Byron")