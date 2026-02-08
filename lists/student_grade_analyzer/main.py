print("=== ÖĞRENCİ NOT ANALİZ SİSTEMİ ===")

notlar = []

ogrenci_sayisi = int(input("Kaç öğrenci var? "))

for i in range(ogrenci_sayisi):
    not_degeri = int(input(f"{i + 1}. öğrencinin notunu giriniz: "))
    notlar.append(not_degeri)

toplam = 0
en_yuksek = notlar[0]
en_dusuk = notlar[0]
gecen_sayisi = 0
kalan_sayisi = 0

for not_degeri in notlar:
    toplam += not_degeri

    if not_degeri > en_yuksek:
        en_yuksek = not_degeri

    if not_degeri < en_dusuk:
        en_dusuk = not_degeri

    if not_degeri >= 50:
        gecen_sayisi += 1
    else:
        kalan_sayisi += 1

ortalama = toplam / len(notlar)

print("\n--- SONUÇLAR ---")
print(f"Ortalama Not: {ortalama:.2f}")
print(f"En Yüksek Not: {en_yuksek}")
print(f"En Düşük Not: {en_dusuk}")
print(f"Geçen Öğrenci Sayısı: {gecen_sayisi}")
print(f"Kalan Öğrenci Sayısı: {kalan_sayisi}")

print("\nGirilen Notlar:")
for not_degeri in notlar:
    print(not_degeri)