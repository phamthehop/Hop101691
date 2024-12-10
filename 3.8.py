def muoisanghai(n):
    if n == 0:  
        return "0"
    nhiphan = ""
    while n > 0:
        nhiphan = str(n % 2) + nhiphan
        n // = 2
    return nhiphan

n = int(input())
kq = muoisanghai(n)
print(kq)
