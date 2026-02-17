# 🚗 Rent A Car — Python Console Application

This project is a console-based car rental management system developed in Python.  
It demonstrates how functions can be used to separate business logic, organize calculations, and manage data in a structured way.

The application allows users to create rental records and list rented vehicles through a simple interactive menu.

---

## 🎯 Purpose of This Project

- Practice writing and using functions  
- Separate calculation logic from program flow  
- Work with dictionaries and lists  
- Simulate a real-world rental scenario  
- Apply conditional pricing rules  

---

## 🧠 Features

### Vehicle Types

The system supports two vehicle categories:

Binek (Passenger Car)  
- Daily price: 400 TL  
- 10% discount if rental period is more than 7 days  

Ticari (Commercial Vehicle)  
- Daily price: 700 TL  
- 20% VAT (KDV) added to total price  

---

## ⚙️ Functional Structure

The program is built using modular functions:

- binek_hesabi(gun, gunluk_ucret)  
  Calculates total cost for passenger vehicles and applies discount if applicable.

- ticari_hesabi(gun, gunluk_ucret)  
  Calculates total cost for commercial vehicles including VAT.

- arac_kaydi()  
  Collects customer information and stores rental data.

- arac_listesi()  
  Displays all registered rental records.

All rental data is stored in a list of dictionaries:

kiralanan_araclar = [
    {
        "ad": "...",
        "tip": "...",
        "gun": ...,
        "ucret": ...
    }
]

---

## 📋 Menu Structure

The application runs in a loop and provides the following options:

1. Kiralama Kaydı Oluşturma  
2. Kiralanan Araç Listesi  
3. Çıkış  

---

## 🖥 Example Flow

--- MENÜ ---
1. Kiralama Kaydı Oluşturma
2. Kiralanan Araç Listesi
3. Çıkış

Müşteri İsim Soyisim: Ahmet Yılmaz  
Araç Tipi: Binek  
Kaç gün: 10  

Kayıt Başarılı! Toplam Tutar: 3600 TL  

---

## 📂 Folder Structure

functions/
└── rent_a_car/
    ├── main.py
    └── README.md

---

## 🚀 How to Run

1. Open the project in any Python IDE (PyCharm, VS Code, etc.)  
2. Run main.py  
3. Follow the menu instructions  

---

## 💡 Concepts Practiced

- Function-based program design  
- Conditional pricing logic  
- Lists and dictionaries  
- Console menu systems  
- Real-world business rule implementation  

---

This project represents a practical example of how modular functions can structure a real-world rental system in Python.