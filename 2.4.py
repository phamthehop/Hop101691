import math

a = int(input())
b = int(input())
c = int(input())

if a == 0:
    if b == 0:
        if c == 0:
            print("VSN")
        else:
            print("VN")
    else:
        x = -c / b
        print(f"x = {x:.2f}")
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"x = {x:.2f}")
    else:
        print("VN")
