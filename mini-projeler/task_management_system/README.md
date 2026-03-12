# ✅ Task Management System — Python Console Application

This project is a robust, file-based task management system developed in Python. Unlike basic memory-only applications, this version ensures data persistence by automatically loading from and saving to a text file.

The application follows a procedural programming approach, focusing on clean function structures and reliable file handling without external dependencies.

---

## 🎯 Project Purpose

- Practice persistent data storage using file I/O  
- Implement error handling using `try-except` for file operations  
- Manage data flow between external files and internal lists  
- Create a clean, user-friendly Command Line Interface (CLI)  
- Strengthen functional programming logic in Python  

---

## ⚙️ How the System Works

When the program starts, it automatically attempts to retrieve previous data from `tasks.txt`. It then presents a menu-driven interface:

1. **Ekleme**: Adds a new task to the current session.  
2. **Listeleme**: Displays all tasks with their corresponding index numbers.  
3. **Kaydet ve Çık**: Commits all changes to the text file and safely exits.

The program ensures that no data is lost by managing the "save" operation during the exit phase.

---

## 📌 Features

### 1️⃣ Persistent Data Storage
- Uses a local `tasks.txt` file to store entries.
- Implementation of `try-except` allows the program to run even if the data file is missing (it creates a new one upon saving).
- Encodes data in **UTF-8** to support various characters.

---

### 2️⃣ Functional Task Management
- **Add Task**: Strips whitespace and validates input before appending to the list.
- **List Tasks**: Provides a formatted output for better readability.
- **Save Logic**: Uses a loop-based writing method to ensure each task is stored on a new line.

---

### 3️⃣ File Integrity & Loading
- Automatically filters out empty lines during the loading process.
- Informs the user when data is successfully synchronized from the disk.

---

## 🧠 Key Concepts Used

- **File I/O**: Reading (`r`) and writing (`w`) modes.  
- **Error Handling**: Managing `FileNotFoundError` without the `os` module.  
- **List Comprehension**: Efficiently processing file lines into Python lists.  
- **Functional Decomposition**: Breaking down tasks into specific, reusable functions.  
- **Input Sanitization**: Ensuring clean data using `.strip()`.

---

## 📂 Project Structure

mini-projeler/  
└── task_management_system/  
    ├── main.py  
    ├── tasks.txt (Auto-generated)  
    └── README.md  

---

## ▶️ How to Run

Run the program using:

```bash
   python main.py