import sys, math
lx, ly, tx, ty = [int(i) for i in input().split()]
DX = lx - tx
DY = ly - ty
while True:
    E = int(input())
    v, h = "", ""
    if DX > 0:
        h = "E"
        DX += 1 
    elif DX < 0:
        h = "W"
        DX -= 1
    if DY > 0:
        v = "S"
        DY -= 1 
    elif DY < 0:
        v = "N"
        DY += 1
    print(v+h)
