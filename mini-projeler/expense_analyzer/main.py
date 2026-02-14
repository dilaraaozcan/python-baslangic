print("=== Bütçe Hesaplayıcı ===")

harcamalar = {
    "Yemek": [],
    "Ulaşım": [],
    "Eğlence": [],
    "Ders": []
}

kategori_listesi = list(harcamalar.keys())

while True:
    print("\n--- Kategori Seç ---")
    for i, kategori in enumerate(kategori_listesi, start=1):
        print(f"{i}. {kategori}")

    secim = int(input("Seçiminiz (çıkmak için 0): "))

    if secim == 0:
        break

    if 1 <= secim <= len(kategori_listesi):
        secilen_kategori = kategori_listesi[secim - 1]

        gun_sayisi = int(input(f"{secilen_kategori} için kaç günlük veri gireceksiniz?: "))

        for gun in range(1, gun_sayisi + 1):
            tutar = float(input(f"{gun}. gün harcaması: "))
            harcamalar[secilen_kategori].append(tutar)

    else:
        print("Geçersiz seçim!")

toplamlar = {kategori: sum(liste) for kategori, liste in harcamalar.items()}
genel_toplam = sum(toplamlar.values())

print("\n=== Haftalık Özet ===")
for kategori, toplam in toplamlar.items():
    print(f"{kategori} : {toplam:.2f} TL")

print(f"GENEL TOPLAM : {genel_toplam:.2f} TL")

if genel_toplam > 0:
    print("\n=== Kategori Yüzdeleri ===")
    for kategori, toplam in toplamlar.items():
        yuzde = (toplam / genel_toplam) * 100
        print(f"{kategori} : %{yuzde:.1f}")

    en_yuksek = max(toplamlar, key=toplamlar.get)
    print(f"\nEn çok harcama yapılan kategori: {en_yuksek}")
else:
    print("Hiç harcama girilmedi.")