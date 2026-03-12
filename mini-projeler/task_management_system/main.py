def verileri_yukle(dosya_adi):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as kaynak:
            return [satir.strip() for satir in kaynak if satir.strip()]
    except FileNotFoundError:
        return []

def verileri_kaydet(dosya_adi, gorev_listesi):
    with open(dosya_adi, "w", encoding="utf-8") as hedef:
        for madde in gorev_listesi:
            hedef.write(f"{madde}\n")

def yeni_is_ekle(gorev_listesi):
    girdi = input("Görev içeriği: ").strip()
    if girdi:
        gorev_listesi.append(girdi)
        print(">> Başarıyla eklendi.")

def listeyi_yazdir(gorev_listesi):
    if not gorev_listesi:
        print(">> Liste şu an boş.")
    else:
        print("\n--- GÖREV LİSTESİ ---")
        for sira, icerik in enumerate(gorev_listesi, 1):
            print(f"{sira}. {icerik}")

def main():
    dosya_yolu = "tasks.txt"
    is_listesi = verileri_yukle(dosya_yolu)

    while True:
        print("\n[1] Ekle | [2] Listele | [3] Kaydet ve Çık")
        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            yeni_is_ekle(is_listesi)
        elif secim == "2":
            listeyi_yazdir(is_listesi)
        elif secim == "3":
            verileri_kaydet(dosya_yolu, is_listesi)
            print("Veriler kaydedildi, hoşça kalın.")
            break
        else:
            print("Hatalı işlem.")

if __name__ == "__main__":
    main()