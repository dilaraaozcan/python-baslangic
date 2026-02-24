# ✅ To-Do App — Python Console Application

This project is a simple console-based task management system developed in Python.  
It allows users to add tasks, list existing tasks, delete tasks, and exit the program through a menu-driven interface.

The application stores tasks dynamically in a list of dictionaries and manages task states in real time.

---

## 🎯 Project Purpose

- Practice working with lists and dictionaries  
- Build a menu-driven console application  
- Implement dynamic data manipulation  
- Strengthen input validation using try-except  
- Simulate a basic task management workflow  

---

## ⚙️ How the System Works

When the program starts, it displays the following menu:

1. Görev Ekle  
2. Görevleri Listele  
3. Görev Sil  
4. Çıkış  

The program continues running until the user selects the exit option.

---

## 📌 Features

### 1️⃣ Add Task
- User enters a task description  
- The task is stored as a dictionary:

  {
    "Görev": task_name,
    "Durumu": False
  }

- Tasks are appended to the `tasks` list  
- Default status is set to **False** (Devam ediyor)

---

### 2️⃣ List Tasks
- Displays all tasks with their current status  
- If task status is `False` → Devam ediyor  
- If task status is `True` → Tamamlandı  
- If no tasks exist, user is informed  

Example output:

1 - Python çalış - Devam ediyor  
2 - Proje bitir - Tamamlandı  

---

### 3️⃣ Delete Task
- Displays tasks with index numbers  
- User selects the task number to delete  
- The selected task is removed using `pop()`  
- Includes input validation for invalid numbers  

If no tasks exist:
Silinecek görev bulunamadı.

---

### 4️⃣ Exit
- Safely terminates the program  

---

## 🧠 Key Concepts Used

- Lists  
- Dictionaries  
- Loop structures (`while`, `for`)  
- Conditional logic (`if-elif-else`)  
- Input validation (`try-except`)  
- List indexing  
- Dynamic data removal  

---

## 📂 Project Structure

mini-projeler/  
└── to_do_app/  
    ├── main.py  
    └── README.md  

---

## ▶️ How to Run

Run the program using:

python main.py

Follow the on-screen instructions to manage your tasks.

---

## 🚀 Why This Project Matters

This project demonstrates how dynamic data structures can be used to simulate a basic productivity application.  
It strengthens understanding of:

- Real-time data updates  
- User interaction handling  
- Clean console-based UI flow  
- State management using boolean values  

It serves as a foundational step toward building more advanced task management systems.