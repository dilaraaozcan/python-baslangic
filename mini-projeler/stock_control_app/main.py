print("=== STOCK CONTROL APP ===")
urun_stok_list = {}

while True:
    print("--- MENÜ ---")
    print("1. Ürün Ekle")
    print("2. Ürün Listele")
    print("3. Ürün Sil")
    print("4. Ürün Güncelle")
    print("5. Çıkış")
    secim = int(input("Seçiminizi giriniz: "))

    try:
        if secim == 1:
            urun_sayisi = int(input("Kaç adet ürün girmek istediğinizi yazınız: "))
            for _ in range(urun_sayisi):
                urun = input("Eklemek istediğiniz ürünü giriniz: ")
                stok = int(input("Stok adedini giriniz: "))

                if urun not in urun_stok_list:
                    urun_stok_list[urun] = stok
                else:
                    print(f"Bu ürün zaten mevcut {urun} -> {urun_stok_list[urun]}")

        elif secim == 2:
            if not urun_stok_list:
                print("Stokta hiç ürün yok! ")
            else:
                print("\n--- Güncel Stok Listesi ---")
                for urun, adet in urun_stok_list.items():
                    print(f"- {urun}: {adet} adet")

        elif secim == 3:
            silinecek_urun = input("Silmek istediğiniz ürünün numarasını yazınız: ")

            if silinecek_urun in urun_stok_list:
                urun_stok_list.pop(silinecek_urun)
                print(f"{silinecek_urun} sistemden silindi.")
            else:
                print("HATA: Bu ürün mevcut değil!")

        elif secim == 4:
            urun_adi = input("Güncellemek istediğiniz ürünün adını giriniz: ")

            if urun_adi in urun_stok_list:
                mevcut = urun_stok_list[urun_adi]
                ekleme_miktari = int(input(f"Mevcut {urun_adi} stoğu: {mevcut} "))
                urun_stok_list[urun_adi] += ekleme_miktari
                print(f"Güncel stok: {urun_adi} -> {urun_stok_list[urun_adi]}")
            else:
                print("HATA: Bu ürün stokta kayıtlı değil!")

        elif secim == 5:
            print("Sistemden başarıyla çıkış yapıldı!")
            break

        else:
            print("Lütfen seçeneklerden (1-5) birisini seçiniz: ")

    except ValueError:
        print("GEÇERSİZ GİRİŞ: Lütfen sadece sayısal değer giriniz: ")
