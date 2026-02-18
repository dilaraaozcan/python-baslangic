# 🏥 Mini Hospital Scheduler — Python Console Application

This project is a console-based hospital appointment scheduling system developed in Python. It analyzes the patient’s complaint, recommends the appropriate medical department, lists available doctors, and allows the user to book an appointment by selecting an available time slot. The system dynamically updates appointment availability after each booking.

---

## 🎯 Purpose of the Project

- Practice working with nested dictionaries  
- Apply string keyword matching logic  
- Use loops and conditional structures effectively  
- Simulate a real-world scheduling system  
- Manage dynamic data updates (removing booked slots)  

---

## ⚙️ How the System Works

### 1️⃣ Complaint Analysis

The user enters a health complaint in text format. The system scans the input for predefined keywords such as:

- "kalp" → Kardiyoloji  
- "ateş" → Dahiliye  
- "diz" → Ortopedi  
- "baş" → Nöroloji  

If no matching keyword is found, the system displays:

Uygun branş bulunamadı.

---

### 2️⃣ Doctor Selection

After determining the appropriate department:

- Available doctors in that branch are listed  
- Only doctors with available time slots are displayed  
- The user selects a doctor by entering a number  
- Input validation ensures correct numeric selection  

---

### 3️⃣ Appointment Time Selection

The system:

- Displays available time slots  
- Allows the user to select one  
- Removes the selected time from the doctor’s schedule  
- Confirms the appointment  

Example confirmation output:

Randevunuz başarıyla oluşturuldu!  
Branş : Kardiyoloji  
Doktor: Prof. Dr. Mustafa Öz  
Saat  : 12:45  

If no time slots remain:

Bu doktorun müsait saati kalmadı.

---

### 4️⃣ Repeat Option

After completing an appointment, the system asks:

Yeni randevu almak ister misiniz? (E/H):

If the user enters anything other than "e", the system exits.

---

## 🧠 Key Concepts Used

- Nested dictionaries  
- List manipulation  
- String matching with `in`  
- Dynamic list updates (removing booked slots)  
- `while` loops  
- `try-except` for input validation  
- Conditional branching  

---

## 📂 Project Structure

mini-projects/  
└── mini_hospital_scheduler/  
    ├── main.py  
    └── README.md  

---

## ▶️ How to Run

Run the program using:

python main.py

Follow the on-screen instructions to create appointments.

---

## 🚀 Why This Project Matters

This project demonstrates how structured data and algorithmic logic can be used to simulate a simplified hospital scheduling system. It strengthens real-world problem modeling, input validation, and dynamic data handling skills.

---