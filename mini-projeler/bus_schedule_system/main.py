print("=== BUS SCHEDULE SYSTEM ===")

seferler = {
    ("Merkez", "Üniversite") : ["06.30","06.45","07.00","07.30","07.45","08.00","08.15","08.30"],
    ("Üniversite", "Merkez") : ["12.00","12.30","13.00","13.30","14.00","14.30","15.00","15.45"],
    ("Merkez", "Hastane") : ["09.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00"],
    ("Hastane", "Merkez") : ["12.00","13.00","14.30","15.00","16.00","18.00","19.45","21.30"],
    ("Üniversite", "Hastane") : ["07.30","08.30","09.30","10.30","11.30","12.30","13.45","14.00"],
    ("Hastane", "Üniversite") : ["09.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00"]
}

while True:
    print("\n--- MENÜ ---")
    print("1. Sefer saati sorgula")
    print("2. Tüm hatları göster")
    print("3. Çıkış")
    secim = input("Seçiminizi (1-3) giriniz: ")

    try:
        if secim == "1":
            kalkis = input("Kalkış Durağı: ").title()
            varis = input("Varış Durağı: ").title()

            hat = (kalkis,varis)

            if hat not in seferler:
                print("Bu hatta sefer bulunamadı!")
            else:
                saatler = seferler[hat]
                print("\nSefer saatleri:")

                for saat in saatler:
                    print(saat)

            kullanici_saati = input("Şu an saat kaç?: ")
            en_yakin = None

            for saat in saatler:
                if saat >= kullanici_saati:
                    en_yakin = saat
                    break

            if en_yakin:
                print(f"En yakın otobüs: {en_yakin}")
            else:
                print("Bugün başka sefer kalmadı.")

        elif secim == "2":
            print("\nBütün Hatlar ")
            for hat in seferler:
                print(hat[0], "->", hat[1])

        elif secim == "3":
            print("Başarıyla çıkış yapılıyor!")
            break

        else:
            print("HATA: Lütfen seçeneklerden (1-3) birisini giriniz: ")

    except ValueError:
        print("Lütfen bir metin ifadesi giriniz: ")
