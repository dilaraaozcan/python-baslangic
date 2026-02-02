import math as m

print("\n=== SAYI ANALİZİ ===")

while True:
    sayi = int(input("Bir tam sayı giriniz: "))

    print("\n---MENÜ---")
    print("1. Asal Sayı Kontrolü")
    print("2. Sayının Faktöriyeli")
    print("3. Armstrong Sayı Kontrolü")
    print("4. Çıkış")
    secim = int(input("Seçiminiz: "))

    if secim == 1:
        sayac = 0
        for i in range(2, sayi):
            if sayi % i == 0:
                sayac += 1
                break

        if sayac == 0 and sayi > 1:
            print(f"{sayi} asal sayıdır.")
        else :
            print(f"{sayi} asal sayı değildir.")

    elif secim == 2:
        sonuc = 1
        for i in range(1, sayi+1):
            sonuc *= i
        print(f"Sonuc: {sonuc}")

    elif secim == 3:
        orj_sayi = sayi
        toplam = 0
        basamak_sayisi = len(str(sayi))
        while orj_sayi > 0:
            basamak = orj_sayi % 10
            toplam += basamak ** basamak_sayisi
            orj_sayi //= 10

        if toplam == sayi:
            print(f"{sayi} armstrong sayıdır.")
        else :
            print(f"{sayi} armstrong sayı değildir.")
    elif secim == 4:
        print("Başarıyla çıkış yapıldı!")
        break
    else :
        print("Hata: lütfen menüdeki (1-4) seçeneklerden birisini seçiniz: ")

