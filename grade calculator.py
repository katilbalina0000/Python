notlar = [99, 78, 92, 34, 67, 88, 69, 76, 50, 39, 39, 41]
toplam = 0
not_sayısı = 0
print("alınan tüm notlar")
for(x) in(notlar):
    print(x)
    toplam = toplam + x
    not_sayısı += 1
print("notların toplamı =", toplam)
print("sınav adedi =", not_sayısı)
print("not ortalaması =", toplam / not_sayısı)
print("not ortalaması =", toplam / not_sayısı)
print("geçen notlar")
y = 0
for(x) in(notlar):
    if(x >= 50): 
        print(x)
        y += 1
print("geçen not adedi=", y)
print("geçmeyen notlar")
z = 0
for(x) in(notlar):
    if(x < 50): 
        print(x)
        z += 1
print("geçemeyen not adedi =", z)
t = 0
for(x) in(notlar):
    if x > t:
        t = x
print("en yüksek not =", t)