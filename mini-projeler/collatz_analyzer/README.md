# 🔢 Collatz Analyzer — 3n + 1 Sequence Analysis (Python)

This project is a **Python console-based analysis tool** built around the famous **Collatz Conjecture (3n + 1 problem)**.  
The program takes a positive integer from the user and repeatedly applies the Collatz rules until the number reaches **1**, while collecting detailed statistics about the process.

The application is interactive, safe against invalid input, and provides a clear step-by-step analysis report.

---

## 🎯 Purpose of This Project

- Understand and apply the Collatz Conjecture algorithm  
- Practice loop-based numerical analysis  
- Track statistics during iterative processes  
- Improve algorithmic thinking with real-time feedback  
- Build a complete, interactive console mini project  

---

## 🔍 Collatz Rules

For a given positive integer **n**:

- If **n is even** → n = n / 2  
- If **n is odd** → n = 3n + 1  

These steps are repeated until the value reaches **1**.

---

## ⚙️ Program Features

- Accepts user input continuously  
- Allows safe exit using the **q** key  
- Validates positive integer input  
- Prints each step of the sequence  
- Calculates:
  - Total number of steps  
  - Maximum value reached  
  - Count of odd-number operations  
  - Count of even-number operations  
- Displays a final summary report  

---

## 🧠 Python Concepts Practiced

- Infinite loops (`while True`)  
- Conditional logic (`if`, `else`)  
- Nested loops  
- Integer arithmetic  
- Input validation with `try–except`  
- Runtime statistics tracking  
- Interactive console output  

---

## 🖥 Sample Program Flow

=== COLLATZ ANALYZER ===  

Enter a number: 12  

1. step → New value: 6  
2. step → New value: 3  
3. step → New value: 10  
4. step → New value: 5  
5. step → New value: 16  
6. step → New value: 8  
7. step → New value: 4  
8. step → New value: 2  
9. step → New value: 1  

--- REPORT ---  
Starting number: 12  
Total steps: 9  
Maximum value reached: 16  
Odd operations count: 3  
Even operations count: 7  

---

## 📂 File Structure

mini-projects/  
└── collatz_analyzer/  
    ├── main.py  
    └── README.md  

---

## 🚀 How to Run

1. Navigate to the `collatz_analyzer` folder  
2. Run the program using Python:
   python main.py  
3. Enter a positive integer or press **q** to exit  

---

## 🎯 Learning Outcome

This project demonstrates how iterative algorithms can be analyzed in depth using Python.  
It combines loops, conditions, input validation, and statistical tracking into a single, well-structured mini project.

---