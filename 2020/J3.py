n = int(input())

pointsX = []
pointsY = []
for i in range(n):
  x,y = input().split(",")
  pointsX.append(x)
  pointsY.append(y)

pointsX.sort()
pointsY.sort()

print(str(int(pointsX[0])-1) +","+str(int(pointsY[0])-1))
print(str(int(pointsX[-1])+1)+ ","+str(int(pointsY[-1])+1))
