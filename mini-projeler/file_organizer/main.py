import os
import shutil

print("=== FILE ORGANIZER ===")

while True:
    print("\n--- MENÜ ---")
    print("1) Klasörü düzenle")
    print("2) Çıkış")

    secim = input("Seçim: ")

    if secim == "2":
        print("Çıkış yapılıyor...")
        break

    if secim != "1":
        print("Geçersiz seçim.")
        continue

    klasor = input("Düzenlenecek klasör yolunu giriniz: ").strip()

    if not os.path.exists(klasor):
        print("Klasör bulunamadı.")
        continue

    try:
        dosyalar = os.listdir(klasor)
    except Exception:
        print("Klasör okunamadı.")
        continue

    tasinan = 0

    for dosya in dosyalar:
        kaynak = os.path.join(klasor, dosya)

        if not os.path.isfile(kaynak):
            continue

        d = dosya.lower()

        if d.endswith(".pdf"):
            hedef_klasor_adi = "PDF"
        elif d.endswith(".jpg") or d.endswith(".jpeg") or d.endswith(".png"):
            hedef_klasor_adi = "Images"
        elif d.endswith(".py"):
            hedef_klasor_adi = "Python"
        elif d.endswith(".txt"):
            hedef_klasor_adi = "Text"
        else:
            hedef_klasor_adi = "Others"

        hedef_klasor = os.path.join(klasor, hedef_klasor_adi)

        if not os.path.exists(hedef_klasor):
            os.mkdir(hedef_klasor)

        hedef = os.path.join(hedef_klasor, dosya)

        try:
            shutil.move(kaynak, hedef)
            tasinan += 1
        except Exception:
            print("Taşınamadı:", dosya)

    print("İşlem bitti. Taşınan dosya sayısı:", tasinan)
