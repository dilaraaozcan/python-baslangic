print("=== TO-DO APP ===")

tasks = []

while True:
    print("---MENÜ---")
    print("1. Görev Ekle")
    print("2. Görevleri Listele")
    print("3. Görev Sil")
    print("4. Çıkış")

    try:
        secim = int(input("Seçiminizi giriniz: "))
    except ValueError:
        print("HATA: Lütfen seçeneklerden (1-4) birisini giriniz.")
        continue

    if secim == 1:
        gorev = input("Eklemek istediğiniz görevi giriniz: ")
        yeni_gorev = {"Görev": gorev, "Durumu": False}
        tasks.append(yeni_gorev)
        print("Görev başarıyla eklendi.")

    elif secim == 2:
        if not tasks:
            print("Henüz yapılacak bir görev yok.")
        else:
            for i in range(len(tasks)):
                if tasks[i]["Durumu"]:
                    durum = "Tamamlandı"
                else:
                    durum = "Devam ediyor"
                print(i + 1, "-", tasks[i]["Görev"], "-", durum)

    elif secim == 3:
        if not tasks:
            print("Silinecek görev bulunamadı.")
        else:
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i]["Görev"])

            try:
                numara = int(input("Silmek istediğiniz görev numarasını yazınız: "))
                if 1 <= numara <= len(tasks):
                    silinen_gorev = tasks.pop(numara-1)
                    print("Silinen:", silinen_gorev["Görev"])
                else:
                    print("HATA: Geçersiz numara!")
            except ValueError:
                print("Lütfen geçerli bir numara giriniz.")

    elif secim == 4:
        print("Başarıyla çıkış yapıldı!")
        break

    else:
        print("HATA! Lütfen seçeneklerden (1-4) birisini seçiniz.")