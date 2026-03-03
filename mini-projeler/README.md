# 🚀 Mini Projects — Python Console Applications

This folder contains practical, console-based mini projects developed while learning Python fundamentals.  
Each project focuses on applying core programming concepts to real-world inspired problems.

The goal of this section is not just syntax practice — but building structured, interactive systems using clean logic and organized data structures.

---

## 🎯 Purpose of This Folder

- Reinforce Python fundamentals through hands-on projects  
- Practice real-world problem modeling  
- Improve algorithmic thinking  
- Strengthen data structure usage (lists, dictionaries)  
- Build structured, portfolio-ready mini systems  

---

## 📂 Included Projects

### ▶️ Collatz Analyzer
Analyzes a number using the 3n+1 (Collatz Conjecture) sequence.

Features:
- Step-by-step sequence generation  
- Total step count  
- Maximum value reached  
- Odd / even step tracking  
- Input validation and safe exit  

Concepts:
- While loops  
- Mathematical logic  
- State tracking  
- Exception handling  

---

### ▶️ Mini Hospital Scheduler
A console-based hospital appointment booking simulation system that dynamically manages departments, doctors, and available time slots.

Features:
- Complaint keyword analysis (e.g., "kalp", "ateş", "diz", "baş")
- Automatic department matching using a mapping dictionary
- Nested dictionary structure for departments → doctors → available time slots
- Dynamic doctor availability filtering
- Time slot booking with automatic removal of selected slots
- Input validation using `try-except`
- Repeat appointment option

Concepts:
- Nested dictionaries
- List filtering
- String matching with `in`
- State mutation (removing booked slots)
- Loop-based interactive system
- Defensive programming (input validation)

This project represents a higher-level structural design compared to basic CRUD mini apps because it simulates a real-world scheduling workflow with dynamic data updates.

---

### ▶️ Simple Library System
A basic library management console app.

Features:
- Add books  
- List books  
- Search books  
- Borrow books (status update)  

Concepts:
- List of dictionaries  
- Enumeration  
- Dynamic state updates  

---

### ▶️ To-Do App
A simple task management system.

Features:
- Add tasks  
- List tasks  
- Delete tasks  
- Status tracking  

Concepts:
- Boolean state management  
- List indexing  
- Try-except validation  

---

### ▶️ Expense Analyzer (Budget Calculator)
Category-based spending tracker.

Features:
- Multiple spending categories  
- Daily expense tracking  
- Category totals  
- Percentage distribution  
- Highest spending category detection  

Concepts:
- Dictionaries with list values  
- Dictionary comprehensions  
- Aggregate calculations  

---

### ▶️ Electric Bill Calculator
Calculates total electricity consumption and billing tier.

Features:
- Multi-day consumption tracking  
- Average usage calculation  
- Tier-based pricing  
- Match-case billing logic  

Concepts:
- List accumulation  
- Conditional pricing  
- Pattern matching  

---

### ▶️ Student Grade Analyzer
Analyzes student grades and generates summary statistics.

Features:
- Average calculation  
- Highest and lowest grade detection  
- Pass / fail classification  
- List traversal  

Concepts:
- Aggregation logic  
- Conditional classification  
- Loop-based data analysis  

---

### ▶️ File Organizer
Organizes files in a selected folder by extension type.

Features:
- Menu-driven folder selection  
- Extension-based categorization  
- Automatic folder creation (PDF / Images / Python / Text / Others)  
- Moves files into categorized folders  
- Reports total moved file count  

Concepts:
- `os` and `shutil` modules  
- File system automation  
- Path handling with `os.path.join()`  
- Conditional classification  
- Exception handling  

---

### ▶️ Stock Control App
A dictionary-based inventory management system.

Features:
- Add products with stock quantities  
- List current stock  
- Delete products  
- Update stock by increasing quantity  
- Input validation with `try-except`  

Concepts:
- Dictionaries (`dict`)  
- CRUD operations  
- Menu-based console flow  
- State updates (incrementing stock)  

---

## 🧠 Core Concepts Covered

- Lists  
- Dictionaries  
- Nested data structures  
- Loops (`for`, `while`)  
- Conditionals (`if-elif-else`)  
- Pattern matching (`match-case`)  
- Exception handling (`try-except`)  
- Mathematical computations  
- Dynamic state management  
- Basic file system scripting (`os`, `shutil`)  

---

## 📂 Folder Structure

mini-projects/  
├── collatz_analyzer/  
├── mini_hospital_scheduler/  
├── simple_library_system/  
├── to_do_app/  
├── expense_analyzer/  
├── electric_bill_calculator/  
├── student_grade_analyzer/  
├── file_organizer/  
├── stock_control_app/  
└── ...  

Each project contains:
- `main.py`  
- `README.md`  

---

## ▶️ How to Run

Navigate into any project folder and run:

python main.py

Each application runs independently.

---

## 🌱 Learning Philosophy

These projects are intentionally designed as small but structured systems.  
The focus is:

- Clean logic  
- Clear menu flow  
- Proper input validation  
- Organized data modeling  

They represent stepping stones toward building larger, more complex applications.

---