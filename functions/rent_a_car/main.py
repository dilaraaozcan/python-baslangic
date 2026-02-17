print("=== RENT A CAR ===")

kiralanan_araclar = []


def binek_hesabi(gun, gunluk_ucret):
    toplam = gun * gunluk_ucret
    if gun > 7:
        toplam -= toplam * 0.10
    return toplam


def ticari_hesabi(gun, gunluk_ucret):
    tutar = gun * gunluk_ucret
    kdv = tutar * 0.20
    toplam = tutar + kdv
    return toplam


def arac_kaydi():
    print("\n--- Yeni Kayıt ---")
    isim = input("Müşteri İsim Soyisim: ")
    arac_tipi = input("Araç Tipi (Binek/Ticari): ").capitalize()
    gun = int(input("Kaç gün kiralayacaksınız?: "))

    hesaplanan_ucret = 0

    if arac_tipi == "Binek":
        gunluk_ucret = 400
        hesaplanan_ucret = binek_hesabi(gun, gunluk_ucret)

    elif arac_tipi == "Ticari":
        gunluk_ucret = 700
        hesaplanan_ucret = ticari_hesabi(gun, gunluk_ucret)

    else:
        print("Hatalı araç tipi girdiniz! Ana menüye dönülüyor...")
        return

    kayit = {
        "ad": isim,
        "tip": arac_tipi,
        "gun": gun,
        "ucret": hesaplanan_ucret
    }
    kiralanan_araclar.append(kayit)
    print(f"Kayıt Başarılı! Toplam Tutar: {hesaplanan_ucret} TL")


def arac_listesi():
    print("\n--- Kiralanan Araç Listesi ---")
    if len(kiralanan_araclar) == 0:
        print("Henüz kayıtlı araç yok.")
    else:
        for arac in kiralanan_araclar:
            print(f"Müşteri: {arac['ad']} | Tip: {arac['tip']} | Gün: {arac['gun']} | Tutar: {arac['ucret']} TL")


while True:
    print("\n--- MENÜ ---")
    print("1. Kiralama Kaydı Oluşturma")
    print("2. Kiralanan Araç Listesi")
    print("3. Çıkış")

    secim = input("Seçiminizi giriniz (1-3): ")

    if secim == '1':
        arac_kaydi()

    elif secim == '2':
        arac_listesi()

    elif secim == '3':
        print("Programdan başarıyla çıkış yapıldı!")
        break

    else:
        print("Hatalı seçim! Lütfen tekrar deneyiniz.")