print("---BMI HESAPLAYICI---")

kilo = float(input("Kilonuzu (kg) giriniz: "))
if kilo < 0:
    print("Kilonuz negatif olamaz!")
    exit()

boy = float(input("Boyunuzu (cm) giriniz: "))
boy /= 100

if boy < 0:
    print("Boyunuz negatif olamaz!")
    exit()

bmi = kilo / pow(boy, 2)

if bmi < 18.5:
    print(f"Vücut kitle indexiniz: {bmi:.2f}, ZAYIF")
    print("Bir uzmanla görüşün!")
elif bmi >= 18.5 and bmi <= 24.9:
    print(f"Vücut kitle indexiniz: {bmi:.2f}, NORMAL")
    print("Gayet normal kilodasınız.")
elif bmi >= 25 and bmi <= 29.9:
    print(f"Vücut kitle indexiniz {bmi:.2f}, FAZLA KİLOLU")
    print("Kilo vermekte fayda var!")
elif bmi > 30:
    print(f"Vücut kitle indexiniz {bmi:.2f}, OBEZ")
    print("Diyete başlamalısınız!!")
else:
    print("Hata")
