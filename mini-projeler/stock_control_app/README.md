# 📦 Stock Control App — Python Console Application

This project is a console-based stock management system developed in Python. It allows users to add products, list current stock, delete products, update stock quantities, and exit the system through a menu-driven interface.

Project location:

mini-projects/
└── stock_control_app/
    ├── main.py
    └── README.md

---

## 🎯 Project Purpose

- Practice working with dictionaries in Python  
- Build a CRUD-style console application  
- Strengthen conditional logic (if-elif-else)  
- Handle user input safely using try-except  
- Simulate a basic inventory management system  

---

## ⚙️ Features

### 1️⃣ Add Product
- User specifies how many products to enter  
- For each product:
  - Product name is entered  
  - Stock quantity is entered  
- If the product does not exist → added to dictionary  
- If it already exists → system warns the user  

Data structure used:
{
    "ProductName": stock_quantity
}

---

### 2️⃣ List Products
- Displays all products and their stock quantities  
- If no products exist → informs the user  

Example output:
--- Güncel Stok Listesi ---
- Elma: 25 adet
- Kalem: 100 adet

---

### 3️⃣ Delete Product
- User enters the product name to delete  
- If product exists → removed from dictionary  
- If not → error message displayed  

---

### 4️⃣ Update Product Stock
- User selects a product  
- Enters additional quantity  
- Stock value is incremented dynamically  

Example:
Mevcut Elma stoğu: 25  
Güncel stok: Elma -> 40  

---

### 5️⃣ Exit
- Terminates the application safely  

---

## 🧠 Concepts Practiced

- Dictionaries (dict)  
- Dictionary key existence checks  
- Loop structures (while, for)  
- Conditional branching  
- Dynamic value updates  
- Exception handling (ValueError)  
- Menu-based system design  

---

## 🔐 Error Handling

The program safely manages:

- Non-numeric menu selections  
- Invalid stock quantities  
- Attempts to delete or update non-existent products  

This ensures the application remains stable during incorrect inputs.

---

## ▶️ How to Run

Navigate to the project folder and execute:

python main.py

Follow the menu instructions to manage stock items.

---

## 🚀 Why This Project Matters

This project simulates a simplified inventory management system. It demonstrates how dictionaries can be used to represent real-world data (product → quantity mapping).

It strengthens:

- Data modeling skills  
- CRUD logic implementation  
- Defensive programming  
- Clean console workflow design  

---