# 📚 Student Course Management System — Python Console Application

This project is a simple **Python console-based application** that allows users to manage a list of courses interactively.  
Users can add new courses, view the current course list, remove existing courses, and safely exit the program through a menu-driven interface.

The application is designed to practice **lists**, **loops**, **input validation**, and Python’s modern **match–case** structure.

---

## 🎯 Application Features

- Add courses dynamically to a list  
- Display all added courses in an ordered format  
- Remove a specific course by name  
- Prevent invalid menu selections  
- Handle empty inputs and missing courses gracefully  
- Exit the program safely when requested  

---

## 🔍 How the Logic Works

- A list (`dersler`) stores all course names  
- The program runs inside an infinite loop (`while True`)  
- A menu is displayed on each iteration  
- User input is validated before processing  
- `match–case` is used to handle menu options clearly  
- Nested loops manage add and delete operations  
- The program exits only when the user selects **Exit**

---

## 🧠 Python Concepts Practiced

- Lists and list operations (`append`, `remove`)  
- Infinite loops (`while True`)  
- Input validation and error handling  
- Conditional logic  
- `match–case` control structure  
- String comparison and user interaction  
- Console-based menu design  

---

## 🖥 Sample Program Flow

=== STUDENT COURSE SYSTEM ===  
1. Add Course  
2. View Courses  
3. Delete Course  
4. Exit  

Selection: 1  
Enter course name: Mathematics  
Mathematics added successfully.

Selection: 2  
1. Mathematics  

Selection: 3  
Enter course name to delete: Mathematics  
Mathematics removed successfully.

Selection: 4  
Exited successfully.

---

## 📂 File Structure

student-course-system/  
└── main.py  
└── README.md  

---

## 🚀 How to Run

1. Open the project folder  
2. Run the program using Python:
   python main.py  
3. Follow the menu instructions in the console  

---

## 🎯 Purpose

This project was created to strengthen fundamental Python skills such as **list management**, **control flow**, and **interactive console programming**.  
It is ideal for beginners who want to practice building structured, menu-driven applications.

---