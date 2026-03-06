# 🚌 Bus Schedule System — Python Console Application

This project is a console-based bus schedule query system developed in Python.  
It allows users to check available bus routes, view departure times for specific routes, and find the nearest upcoming bus based on the current time.

Project location:

mini-projects/
└── bus_schedule_system/
    ├── main.py
    └── README.md

---

## 🎯 Project Purpose

- Practice working with **Python dictionaries**
- Use **tuple keys** for representing routes
- Strengthen **loop and conditional logic**
- Build a **menu-driven console application**
- Implement a simple **nearest-time search algorithm**

---

## ⚙️ Features

### 1️⃣ Bus Schedule Query
Users can enter:

- Departure stop
- Destination stop

The system will:

- Check if the route exists
- Display all departure times for that route
- Ask the current time
- Show the **nearest upcoming bus**

Example:

Kalkış Durağı: Merkez  
Varış Durağı: Üniversite  

Sefer saatleri:  
06.30  
06.45  
07.00  
07.30  
...

En yakın otobüs: 07.30

---

### 2️⃣ Show All Routes

Users can view all available bus routes.

Example:

Merkez -> Üniversite  
Üniversite -> Merkez  
Merkez -> Hastane  
Hastane -> Merkez  

This helps users understand which routes are supported by the system.

---

### 3️⃣ Exit

Safely terminates the application.

---

## 🧠 Concepts Practiced

- Dictionaries (`dict`)
- Tuple keys for route mapping
- Loop iteration (`for`)
- Conditional branching (`if-elif-else`)
- Menu-based program flow
- Simple time comparison logic
- Exception handling (`try-except`)

---

## 📊 Data Structure

Routes are stored using a dictionary where:

- **Key** → `(departure, destination)`
- **Value** → List of departure times

Example structure:

{
("Merkez", "Üniversite"): ["06.30","06.45","07.00"],
("Üniversite", "Merkez"): ["12.00","12.30","13.00"]
}

---

## ▶️ How to Run

Navigate to the project folder and run:

python main.py

Follow the menu instructions to query bus schedules.

---

## 🚀 Why This Project Matters

This project demonstrates how Python dictionaries and loops can be used to simulate a simple **transportation schedule system**.

It strengthens:

- Data modeling with dictionaries
- Searching algorithms
- Menu-based application design
- User interaction in console programs

---