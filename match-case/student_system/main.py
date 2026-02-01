dersler = []

while True:
    print("\n=== ÖĞRENCİ DERS SİSTEMİ ===")
    print("1. Ders Ekle")
    print("2. Dersleri Görüntüle")
    print("3. Ders Sil")
    print("4. Çıkış")

    secim = int(input("Seçiminiz: "))

    if secim < 1 or secim > 4:
        print("Geçersiz seçim, lütfen menüdeki seçeneklerden birisini seçiniz!")
        continue

    match secim:
        case 1:
            while True:
                ders_adi = input(("\nDers ismini giriniz (Çıkmak için '0' a basınız): "))

                if ders_adi == "0":
                    break

                if ders_adi == "":
                    print("Ders adı girilmedi! Lütfen ders adını giriniz: ")
                    continue
                else:
                    dersler.append(ders_adi)
                    print(f"{ders_adi} başarıyla eklendi.")

        case 2:
            if not dersler:
                print("Henüz ders eklenmedi.")
            else:
                print("\n--- Eklenen Dersler ---")
                i = 1
                for ders_adi in dersler:
                    print(f"{i}. {ders_adi}")
                    i += 1

        case 3:
            while True:
                if not dersler:
                    print("Silinecek ders yok.")
                    break

                print(f"\nMevcut Dersleriniz {dersler}.")
                ders_sil = input("Silmek istediğiniz ders adını giriniz (Çıkmak için '0' a basınız): ")

                if ders_sil == "0":
                    break

                if ders_sil in dersler:
                    dersler.remove(ders_sil)
                    print(f"{ders_sil} başarıyla silindi.")
                else:
                    print("Ders bulunamadı!")

        case 4:
            print("Başarıyla çıkış yapıldı!")
            break