row1 = input().split()
row2 = input().split()
row3 = input().split()
row4 = input().split()

matrix = [row1,row2,row3,row4]

cSum = []
rSum = []

for i in range(4):
  valueC = 0
  valueR = 0
  for l in range(4):
    valueC += int(matrix[l][i])
    valueR += int(matrix[i][l])
  cSum.append(valueC)
  rSum.append(valueR)

if cSum[0] == cSum[1] and cSum[1] == cSum[2] and cSum[2] == cSum[3]:
  if rSum[0] == rSum[1] and rSum[1] == rSum[2] and rSum[2] == rSum[3]:
    if rSum[0] == cSum[0]:
      print("magic")
    else:
      print("not magic")
  else:
    print("not magic")
else:
  print("not magic")