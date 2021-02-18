a = []

for i in range(4):
  a.append(int(input()))

def ignore(arr):
  if arr[0] == 8 or arr[0] == 9:
    if arr[-1] == 8 or arr[-1] == 9:
      if arr[1] == arr[2]:
        return 'ignore'
  
  return 'answer'

print(ignore(a))