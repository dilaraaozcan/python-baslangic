# 🔢 Number Analysis Tool — Python Console Application

This project is a **menu-driven Python console application** that performs multiple numerical analyses on a user-entered integer.  
The user can check whether a number is **prime**, calculate its **factorial**, test if it is an **Armstrong number**, or safely exit the program.

The application is designed to practice **loops**, **conditional statements**, **basic algorithms**, and **interactive menu logic** in Python.

---

## 🎯 Application Features

- Accepts an integer input from the user  
- Provides a menu with multiple analysis options  
- Performs:
  - Prime number check  
  - Factorial calculation  
  - Armstrong number verification  
- Runs continuously until the user chooses to exit  
- Displays clear and informative results for each operation  

---

## 🔍 How the Logic Works

- The program runs inside an infinite `while True` loop  
- A number is taken from the user at the start of each cycle  
- A menu is displayed with four options  
- Based on the user’s selection:
  - **Prime Check:** Tests divisibility from 2 to n−1  
  - **Factorial:** Multiplies numbers from 1 to n  
  - **Armstrong Check:**  
    - Calculates the number of digits  
    - Raises each digit to the power of digit count  
    - Compares the sum with the original number  
- The loop terminates only when the **Exit** option is selected  

---

## 🧠 Python Concepts Practiced

- Infinite loops (`while True`)  
- Conditional logic (`if`, `elif`, `else`)  
- `for` and `while` loops  
- Prime number testing algorithm  
- Factorial calculation  
- Armstrong number logic  
- String-to-integer conversion for digit analysis  
- Menu-based console interaction  

---

## 🖥 Sample Program Flow

=== NUMBER ANALYSIS ===  

--- MENU ---  
1. Prime Number Check  
2. Factorial Calculation  
3. Armstrong Number Check  
4. Exit  

Selection: 1  
13 is a prime number.

Selection: 2  
Result: 120  

Selection: 3  
153 is an Armstrong number.

Selection: 4  
Exited successfully.

---

## 📂 File Structure

number-analysis-tool/  
└── main.py  
└── README.md  

---

## 🚀 How to Run

1. Open the project directory  
2. Run the program with Python:
   python main.py  
3. Enter a number and choose an operation from the menu  

---

## 🎯 Purpose

This project was created to reinforce **algorithmic thinking** and **core Python programming skills** through a single, interactive application.  
It combines multiple mathematical concepts into a clean, menu-based structure suitable for beginners.

---
