# 📚 Simple Library System — Python Console Application

This project is a console-based library management system developed in Python.  
It allows users to add books, list available books, search for specific titles, and borrow books through an interactive menu-driven interface.

The system stores book information dynamically using a list of dictionaries and updates book availability status in real time.

---

## 🎯 Purpose of the Project

- Practice working with lists and dictionaries  
- Strengthen menu-based program design  
- Implement search functionality  
- Manage dynamic state updates  
- Apply loop and conditional logic in real-world scenarios  

---

## ⚙️ How the System Works

When the program starts, it displays a menu:

1. Kitap Ekle  
2. Kitapları Listele  
3. Kitap Ara  
4. Kitap Ödünç Al  
5. Çıkış  

The system continues running until the user selects the exit option.

---

## 📖 Features

### 1️⃣ Add Book
- User enters book name and author  
- Book is stored as a dictionary:
  {
    "isim": book_name,
    "yazar": author_name,
    "durum": "Mevcut"
  }
- The book is appended to the `books` list  

---

### 2️⃣ List Books
- Displays all books in the library  
- If no books exist, the system informs the user  

Example output:
Kitap Listesi: {'isim': '1984', 'yazar': 'George Orwell', 'durum': 'Mevcut'}

---

### 3️⃣ Search Book
- User enters the book name  
- The system searches through the list  
- If found, book details are displayed  
- If not found, user is informed  

---

### 4️⃣ Borrow Book
- User enters the book name  
- If the book exists and status is "Mevcut":
  - The system updates status to "Ödünç Verildi"
  - Shows the position (index) of the book  
- If already borrowed:
  - Displays warning message  
- If not found:
  - Displays not found message  

---

### 5️⃣ Exit
- Terminates the program safely  

---

## 🧠 Key Concepts Used

- Lists  
- Dictionaries  
- Nested data structures  
- Loops (`while`, `for`)  
- Conditional logic (`if-elif-else`)  
- Enumeration with `enumerate()`  
- Exception handling (`try-except`)  

---

## 📂 Project Structure

mini-projects/  
└── simple_library_system/  
    ├── main.py  
    └── README.md  

---

## ▶️ How to Run

Run the program using:

python main.py

Follow the on-screen instructions to interact with the system.

---

## 🚀 Why This Project Matters

This project simulates a simplified library automation system.  
It demonstrates how structured data (list + dictionary) can be used to manage real-world entities and how program state changes dynamically over time.

It strengthens:
- Data modeling skills  
- Interactive console design  
- Real-world scenario simulation  
- Clean program flow control

---