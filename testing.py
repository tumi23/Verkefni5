


level = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2],
    [2, 1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 1, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 1, 2],
    [2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], ]

x, y = 0, 0
coordinates = []
for i in range(13):
    sub = []
    x = 0
    for j in range(15):
        sub.append((x,y))
        x += 60
    coordinates.append(sub)
    y += 60

for i in coordinates:
    print(i)

bx = 60
by = 120
bi = 0
bj = 0
print()
for i in range(len(coordinates)):
    if (bx,by) in coordinates[i]:
        print(coordinates[i].index((bx, by)))
        inde = coordinates[i].index((bx, by))
        print (coordinates[i][inde])
        bj = inde
        bi = i


right = coordinates[bi][bj]
for i in range(4):
    if level[bi][bj+i] == 2 or level[bi][bj+i] == 3:
        break
    right = coordinates[bi][bj + i]

left = coordinates[bi][bj]
for i in range(4):
    if level[bi][bj-i] == 2 or level[bi][bj-i] == 3:
        break
    left = coordinates[bi][bj - i]

top = coordinates[bi][bj]
for i in range(4):
    if level[bi+i][bj] == 2 or level[bi+i][bj] == 3:
        break
    top = coordinates[bi + i][bj]

bottom = coordinates[bi][bj]
for i in range(4):
    if level[bi-i][bj] == 2 or level[bi-i][bj] == 3:
        break
    bottom = coordinates[bi - i][bj]






print()
print(right)
print(left)
print(top)
print(bottom)
