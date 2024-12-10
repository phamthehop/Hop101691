a = int(input())
b = int(input())

if a == 0:
    if b > 0:
        print("VSN")
    else:
        print("VN")
else:
    c = -b / a
    if a > 0:
        print(f"x > {c:.2f}")
    else:
        print(f"x < {c:.2f}")
