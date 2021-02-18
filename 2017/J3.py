start = input().split()
end = input().split()
charge = int(input())

difX = int(start[0]) - int(end[0])
if difX < 0:
  difX = difX * -1

difY =  int(start[1]) - int(end[1])
if difY < 0:
  difY = difY * -1

distance = difY + difX

if distance <= charge and ((charge - distance)%2 == 0):
  print('Y')
else:
  print('N')