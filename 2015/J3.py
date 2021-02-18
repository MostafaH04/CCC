consonant = 'bcdfghjklmnpqrstvwxyz'
vowels = 'aeiou'
batches = ['bc', 'dfg','hjkl','mnpqr','stvwxyz']

word = input()

ans = ''

for i in word:
  part = i
  if i not in vowels:
    for x in range(len(batches)):
      if i in batches[x]:
        part += vowels[x]
    if consonant[consonant.index(i,0)] != 'z':
      part += consonant[consonant.index(i,0)+1]
    else:
      part += 'z'
    
  ans += part
  part = ''

print(ans)