distances = input().split()

a = int(distances[0])
b = int(distances[1])
c = int(distances[2])
d = int(distances[3])

print('0 '+ str(a)+ ' '+ str(a+b) + ' '+str(a+b+c)+ ' ' + str(a+b+c+d))

print(str(a)+' 0 '+str(b)+' '+str(b+c)+' '+str(b+c+d))
print(str(a+b)+' '+str(b)+' 0 '+str(c)+' '+ str(c+d))
print(str(a+b+c)+' '+str(b+c)+' '+str(c)+' 0 '+str(d))
print(str(a+b+c+d)+' '+str(b+c+d)+' '+str(c+d)+' '+str(d)+' 0')