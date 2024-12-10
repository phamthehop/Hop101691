def thap_phan_sang_thap_luc_phan(n):
    if n == 0:
        return "0"
    
    hex_map = "0123456789ABCDEF" 
    thap_luc_phan = ""
    
    while n > 0:
        thap_luc_phan = hex_map[n % 16] + thap_luc_phan 
        n //= 16 
    return thap_luc_phan

n = int(input())
ket_qua = thap_phan_sang_thap_luc_phan(n)
print(ket_qua)
