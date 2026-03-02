# 📂 File Organizer — Python Console Application

This project is a console-based file organizing tool developed in Python.  
It automatically categorizes files inside a selected folder based on their file extensions and moves them into appropriate subfolders.

Project location:

mini-projects/  
└── file_organizer/  
    ├── main.py  
    └── README.md  

---

## 🎯 Project Purpose

- Practice file and directory manipulation with Python  
- Learn to use the `os` and `shutil` modules  
- Apply conditional logic to real-world automation  
- Build a practical productivity script  
- Strengthen error handling with `try-except`  

---

## ⚙️ Features

- Menu-driven console interface  
- Validates folder existence before processing  
- Automatically creates categorized subfolders  
- Moves files based on extension type  
- Counts and reports moved files  
- Handles errors safely without crashing  

---

## 📁 File Categorization Rules

Files are organized according to their extensions:

- `.pdf` → **PDF**
- `.jpg`, `.jpeg`, `.png` → **Images**
- `.py` → **Python**
- `.txt` → **Text**
- All other file types → **Others**

Example structure:

Before organizing:

documents/  
  report.pdf  
  image.jpg  
  script.py  
  notes.txt  

After organizing:

documents/  
  PDF/  
    report.pdf  
  Images/  
    image.jpg  
  Python/  
    script.py  
  Text/  
    notes.txt  

---

## 🧠 Concepts Practiced

- `os` module (file & directory operations)  
- `shutil` module (file moving)  
- Path handling with `os.path.join()`  
- File extension detection with `.endswith()`  
- Loop iteration over directory contents  
- Conditional branching (`if-elif-else`)  
- Exception handling (`try-except`)  

---

## 🔐 Error Handling

The program safely manages:

- Invalid folder paths  
- Unreadable directories  
- File move failures  
- Invalid menu selections  

This ensures stable execution and prevents crashes.

---

## ▶️ How to Run

Navigate to the project directory and execute:

python main.py

Then enter the full path of the folder you want to organize.

---

## 🚀 Why This Project Matters

This project demonstrates how Python can interact directly with the file system to automate repetitive tasks.

It strengthens:

- Real-world scripting skills  
- File system automation  
- Clean program structure  
- Defensive programming  

This is a practical example of turning basic programming knowledge into useful automation.

---
