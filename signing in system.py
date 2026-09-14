isim = input("adın ne?") 
şifre = input("şifre giriniz")
kalan_deneme_hakkı = 3
while (şifre != "Muhammedgok123." or isim != "Muhammed") and 1 <= kalan_deneme_hakkı <= 3:
    kalan_deneme_hakkı -= 1
    if(kalan_deneme_hakkı > 0):
        print("kullanıcı adı veya şifre yanlış")
        print("tekrar deneyiniz")
        print("kalan deneme hakkı =", kalan_deneme_hakkı)
        isim = input("adın ne?") 
        şifre = input("şifre giriniz")
if(şifre != "Muhammedgok123." or isim != "Muhammed"and kalan_deneme_hakkı <= 1):
    print("deneme hakkın doldu")
if( isim == "Muhammed" and şifre == "Muhammedgok123.") :
    süre = int(input("kaç saat ders çalıştın"))
    if(süre>=7): print("gardaş yavaş git makine gibi çalışıyorsun")
    elif(7>=süre>3 ): print("idare idare")
    else: print("gardaş biraz daha çalışsana")
