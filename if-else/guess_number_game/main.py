import random

print("=== SAYI TAHMİN OYUNU ===")
skorlar = []

while True:
    print("---MENÜ---")
    print("1. Oyna")
    print("2. Skorlar")
    print("3. Çıkış")

    try:
        secim = int(input("Seçiminizi giriniz: "))

        if secim == 1:
            hedef = random.randint(1,100)
            deneme = 0
            hak = 10

            while hak > 0:
                print(f"Kalan hakkınız: {hak}")
                try:
                    tahmin = int(input("Tahmininizi giriniz: "))
                    deneme += 1
                    hak -= 1

                    if tahmin < hedef:
                        if hak > 0:
                            print("Yaklaştınız! Daha büyük bir sayı giriniz: ")
                        else:
                            print(f"Hakkınız bitti, sayı buydu: {hedef}")

                    elif tahmin > hedef:
                        if hak > 0:
                            print("Yaklaştınız! Daha küçük bir sayı giriniz: ")
                        else:
                            print(f"Hakkınız bitti, sayı buydu: {hedef}")

                    elif tahmin == hedef:
                        print("Tebrikler! Doğru tahmin")
                        skorlar.append(deneme)
                        break

                except ValueError:
                    print("HATA! Lütfen bir tam sayı giriniz: ")

        elif secim == 2:
            if not skorlar:
                print("Henüz kaydedilmiş liste yok!")
            else:
                skorlar.sort()
                print("--- EN İYİ SKORLAR ---")
                for i, skor in enumerate(skorlar, start=1):
                    print(f"{i}. Oyun: {skor} deneme")

        elif secim == 3:
            print("Başarıyla çıkış yapıldı!")
            break

        else:
            print("HATA! Lütfen seçeneklerden (1-3) birisini seçiniz: ")

    except ValueError:
        print("HATA! Lütfen seçeneklerden (1-3) birisini seçiniz: ")
