icon = [['*','x','*'],[' ','x','x'], ['*', ' ', '*']]

k = int(input())

tempHolder = ''
newIcon = []

for i in icon:
    for x in i:
        for l in range(k):
            tempHolder += x
    
    newIcon.append(tempHolder)
    tempHolder = ''


lastIcon = []
for i in newIcon:
    for l in range(k):
        print(i)
