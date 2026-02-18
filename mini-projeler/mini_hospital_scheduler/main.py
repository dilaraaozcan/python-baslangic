print("=== MINI HOSPITAL SCHEDULER ===")

doktorlar = {
    "Kardiyoloji": {
        "Prof. Dr. Mustafa Öz": ["09:00", "12:45", "15:20", "16:00"],
        "Doç. Dr. Ahmet Ata": ["10:00", "13:00", "14:00"],
        "Op. Dr. Mine Turgut": ["11:30", "14:45", "16:30"]
    },
    "Dahiliye": {
        "Prof. Dr. Defne Duman": ["09:00", "10:15", "11:00"],
        "Doç. Dr. İrem Baykar": ["10:00", "10:45", "11:45"],
        "Op. Dr. Ege Sert": ["09:30", "14:45", "16:30"]
    },
    "Ortopedi": {
        "Prof. Dr. Emre Kara": ["10:30", "13:45", "14:30"],
        "Doç. Dr. Numan Uras": ["09:00", "10:45", "12:15"],
        "Op. Dr. Merve Ufuk": ["11:00", "12:00", "13:00"]
    },
    "Nöroloji": {
        "Prof. Dr. Asaf Er": ["09:00", "12:00", "15:00"],
        "Doç. Dr. Eymen Yazıcıoğlu": ["10:00", "12:15", "14:45"],
        "Op. Dr. Akif Barçın": ["09:00", "10:00", "12:45"]
    }
}

hastalik_map = {
    "kalp": "Kardiyoloji",
    "göğüs": "Kardiyoloji",
    "ateş": "Dahiliye",
    "mide": "Dahiliye",
    "diz": "Ortopedi",
    "baş": "Nöroloji"
}

while True:
    hastalik = input("\nSağlık sorununuzu yazınız: ").lower()
    bulunan_brans = None

    for kelime in hastalik_map:
        if kelime in hastalik:
            bulunan_brans = hastalik_map[kelime]
            break

    if not bulunan_brans:
        print("Uygun branş bulunamadı.")
        continue

    print("Önerilen branş:", bulunan_brans)

    doktor_listesi = list(doktorlar[bulunan_brans].keys())
    uygun_doktorlar = []

    for doktor in doktor_listesi:
        if doktorlar[bulunan_brans][doktor]:
            uygun_doktorlar.append(doktor)

    if not uygun_doktorlar:
        print("Bu branşta müsait doktor yok.")
        continue

    while True:
        print("\nMevcut doktorlar:")
        for i, doktor in enumerate(uygun_doktorlar, 1):
            print(i, "-", doktor)

        try:
            secim = int(input("Doktor seçiniz: "))
            if 1 <= secim <= len(uygun_doktorlar):
                secilen_doktor = uygun_doktorlar[secim - 1]
                break
            else:
                print("Geçersiz seçim.")
        except ValueError:
            print("Lütfen sayı giriniz.")

    saatler = doktorlar[bulunan_brans][secilen_doktor]

    while True:
        if not saatler:
            print("Bu doktorun müsait saati kalmadı.")
            break

        print("\nMüsait saatler:")
        for i, saat in enumerate(saatler, 1):
            print(i, "-", saat)

        try:
            saat_secim = int(input("Saat seçiniz: "))
            if 1 <= saat_secim <= len(saatler):
                secilen_saat = saatler[saat_secim - 1]
                saatler.remove(secilen_saat)
                print("\nRandevunuz başarıyla oluşturuldu!")
                print("Branş :", bulunan_brans)
                print("Doktor:", secilen_doktor)
                print("Saat  :", secilen_saat)
                break
            else:
                print("Geçersiz saat seçimi.")
        except ValueError:
            print("Lütfen sayı giriniz.")

    devam = input("\nYeni randevu almak ister misiniz? (E/H): ").lower()
    if devam != "e":
        print("Sağlıklı günler dileriz!")
        break