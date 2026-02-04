import math

def daire_alan(r):
    return math.pi * math.pow(r, 2)
def kare_alan(kenar):
    return math.pow(kenar, 2)
def dikdortgen_alan(kisa_kenar, uzun_kenar):
    return kisa_kenar * uzun_kenar
def ucgen_alan(kenar, yukseklik):
    return (kenar * yukseklik) / 2
def silindir_alan(yaricap, yukseklik):
    return 2 * math.pi * yaricap * (yaricap + yukseklik)

while True:
    try:

        print("\n=== Geometrik Şekil Alan Hesaplayıcısı ===")
        print("---MENÜ---")
        print("1. Daire alanı")
        print("2. Kare alanı")
        print("3. Dikdörtgen alanı")
        print("4. Üçgen alanı")
        print("5. Silindir alanı")
        print("6. Çıkış")
        secim = int(input("Seçiminizi giriniz: "))

        if secim == 1:
            r = float(input("Dairenin yarıçapını giriniz: "))
            print(f"Dairenin alanı: {daire_alan(r):.2f} dir.")

        elif secim == 2:
            kenar = float(input("Karenin kenar uzunluğunu giriniz: "))
            print(f"Karenin alanı: {kare_alan(kenar):.1f} dir.")

        elif secim == 3:
            while True:
                kisa_kenar = float(input("Dikdörtgenin kısa kenarını giriniz: "))
                uzun_kenar = float(input("Dikdörtgenin uzun kenarını giriniz: "))

                if kisa_kenar > uzun_kenar:
                    print("HATA: Kısa kenar, uzun kenardan uzun olamaz! Lütfen kısa kenarı giriniz: ")

                elif kisa_kenar == uzun_kenar:
                    print("HATA: Bu bir kare değil, lütfen kısa ve uzun kenarı giriniz: ")

                else:
                    print(f"Dikdörtgenin alanı: {dikdortgen_alan(kisa_kenar, uzun_kenar):.2f} dir.")
                    break

        elif secim == 4:
            kenar = float(input("Üçgenin kenar uzunluğunu giriniz: "))
            yukseklik = float(input("Üçgenin yukseklik giriniz: "))

            print(f"Üçgenin alanı: {ucgen_alan(kenar, yukseklik):.2f} dir.")

        elif secim == 5:
            yaricap = float(input("Silindirin yarıçapını giriniz: "))
            yukseklik = float(input("Silindirin yüksekliğini giriniz: "))

            print(f"Silindirin alanı: {silindir_alan(yaricap, yukseklik):.2f} dir.")

        elif secim == 6:
            print("Başarıyla çıkış yapılıyor!")
            break

        else :
            print("Hatalı seçim, lütfen menüdeki (1-6) seçeneklerden birisini seçiniz: ")

    except ValueError:
        print("Geçersiz giriş! Lütfen sadece sayı giriniz: ")
        continue