N, Q = map(int, input().split())

S = input()

for _ in range(Q):
    L, R, C = input().split()
    L, R = int(L), int(R)
    
    ket_qua = S[L-1:R].count(C)

    print(ket_qua)
