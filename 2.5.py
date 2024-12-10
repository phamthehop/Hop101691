a1,b1,c1 = map(int,input().split())
a2,b2,c2 = map(int,input().split())

d = a1 * b2 - a2 * b1
if d != 0:
    x = (c1 * b2 - c2 * b1) / d
    y = (a1 * c2 - a2 * c1) / d
    print(x,y)
else:
    if a1 * c2 - a2 * c1 != b1 * c2 - b2 * c1:
        print("VN")
    else:
        print("VSN")
