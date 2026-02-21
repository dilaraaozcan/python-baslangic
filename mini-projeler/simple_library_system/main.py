print("=== Simple Library System ===")
books = []

try:
    while True:
        print("--- MENÜ ---")
        print("1. Kitap Ekle")
        print("2. Kitapları Listele")
        print("3. Kitap Ara")
        print("4. Kitap Ödünç Al")
        print("5. Çıkış")

        secim = int(input("Seçiminizi giriniz: "))

        if secim == 1:
            kitap_adi = input("Eklemek istediğiniz kitabı yazınız: ")
            yazar_adi = input("Yazar adını yazınız: ")
            yeni_kitap = {"isim": kitap_adi, "yazar": yazar_adi, "durum": "Mevcut"}
            books.append(yeni_kitap)
            print("Kitap başarıyla eklendi.")

        elif secim == 2:
            if not books:
                print("Henüz kütüphanede kitap yok!")
            else:
                for kitap in books:
                    print(f"Kitap Listesi: {kitap}")

        elif secim == 3:
            kitap_ismi = input("Aradığınız kitabın adını giriniz: ")
            bulundu = False
            for kitap in books:
                if kitap["isim"] == kitap_ismi:
                    print(f"Aradığınız kitap elimizde mevcut: {kitap}")
                    bulundu = True
                    break
            if not bulundu:
                print("Aradığınız kitap bulunamadı.")

        elif secim == 4:
            odunc_alinan_kitap = input("Ödünç almak istediğiniz kitabın ismini giriniz: ")
            bulundu = False
            for sira, kitap in enumerate(books, start=1):
                if kitap["isim"] == odunc_alinan_kitap:
                    if kitap["durum"] == "Mevcut":
                        print(f"Aradığınız kitabı {sira}. sırada bulabilirsiniz.")
                        kitap["durum"] = "Ödünç Verildi"
                    else:
                        print("Kitap zaten ödünç verilmiş.")
                    bulundu = True
                    break
            if not bulundu:
                print("Aradığınız kitap bulunamadı.")

        elif secim == 5:
            print("Programdan başarıyla çıkış yapıldı!")
            break

        else:
            print("Hatalı seçim, lütfen seçeneklerden (1-5) birisini giriniz: ")

except ValueError:
    print("Lütfen bir tam sayı giriniz!: ")