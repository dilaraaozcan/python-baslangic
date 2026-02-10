print("=== ELEKTRİK FATURASI HESAPLAYICI ===")

tuketim_miktar = []
gun = int(input("Kaç günlük fatura hesabı yapacaksınız, lütfen giriniz: "))

sayac = 0
toplam_tuketim = 0
kademe = ""

while sayac < gun :
    miktar = float(input(f"{sayac+1}. gün tüketim miktarını giriniz: "))
    tuketim_miktar.append(miktar)
    sayac += 1

for sayi in tuketim_miktar:
    toplam_tuketim += sayi

print(f"\nTotal tüketiminiz {toplam_tuketim} birimdir.")

if gun > 0:
    ortalama_miktar = toplam_tuketim / gun
    print(f"Ortalama elektrik tüketim miktarı: {ortalama_miktar:.2f}")

print("--- Kademe Hesabı ---")
if toplam_tuketim < 150 :
    kademe = "Düşük"
    print("Kademe: Düşük")
elif 150 <= toplam_tuketim <= 300:
    kademe = "Orta"
    print("Kademe: Orta")
else:
    kademe = "Yüksek"
    print("Kademe: Yüksek")

match kademe:
    case "Düşük":
        fatura = toplam_tuketim * 1.5
        print(f"Fatura toplamınız {fatura:.2f} TL dir.")
    case "Orta":
        fatura = toplam_tuketim * 2.2
        print(f"Fatura toplamınız {fatura:.2f} TL dir.")
    case "Yüksek":
        fatura = toplam_tuketim * 3.0
        print(f"Fatura toplamınız {fatura:.2f} TL dir.")