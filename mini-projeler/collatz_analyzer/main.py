print("=== COLLATZ ANALYZER ===")

while True:

    try:
        sayi = input("\nLütfen bir tam sayı giriniz, çıkış için 'q' harfine basınız: ")

        if sayi.lower() == 'q':
            print("Programdan çıkılıyor...")
            break

        sayi = int(sayi)

        if sayi <= 0:
            print("HATA: Lütfen pozitif bir tam sayı giriniz! ")
        else:
            baslangic_sayisi = sayi
            steps = 0
            max_value = sayi
            odd_count = 0
            even_count = 0

            while sayi != 1:

                if sayi % 2 == 0:
                    sayi //= 2
                    even_count += 1
                else:
                    sayi = 3 * sayi + 1
                    odd_count += 1

                steps += 1

                if sayi > max_value:
                    max_value = sayi

                print(f"{steps}. adım -> Yeni sayı: {sayi}")

            odd_count += 1

            print("\n--- RAPOR ---")
            print(f"Başlangıç sayısı: {baslangic_sayisi}")
            print(f"Toplam adım sayısı: {steps}")
            print(f"Ulaşılan en büyük değer: {max_value}")
            print(f"Tek sayı adedi: {odd_count}")
            print(f"Çift sayı adedi: {even_count}")
            print("Collatz Analyzer başarıyla tamamlandı!")

    except ValueError:
        print("HATA: Lütfen sadece tam sayı giriniz!")