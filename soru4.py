
liste = 0

for k in range(100, 999, ):
    a = str(k) [0]
    b = str(k) [1]
    c = str(k) [2]
    if a != b and a != c and b != c:
        print(k)
        liste += 1
print("Birbirini tekrar etmeyen sayıların toplamı=", liste)