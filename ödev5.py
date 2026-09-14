import time


sayac = 0
sayı = int(input("bir sayı giriniz"))
while sayı >= 1:
    sayı = sayı - 1
    sayac = sayac + 1
    print(sayı) 
    time.sleep(1)
print("BOOOM!!!"), print(sayac, "adet sayı yazdırıldı")
