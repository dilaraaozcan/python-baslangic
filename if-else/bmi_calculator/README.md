# 🧮 BMI Calculator — Python Console Application

This project is a simple Python console application that calculates the Body Mass Index (BMI) based on user input.
It evaluates the user’s weight and height, computes the BMI value, and classifies the result according to standard BMI categories.

The application focuses on fundamental Python concepts such as user input handling, conditional logic, and mathematical calculations.

---

## 🎯 Purpose of the Project

- Practice handling user input in Python
- Perform mathematical calculations using built-in functions
- Apply conditional statements (if / elif / else)
- Validate user input to prevent invalid values
- Provide meaningful feedback based on calculated results

---

## ⚙️ How the Program Works

1. The user enters their weight in kilograms.
2. The program checks whether the weight value is valid (non-negative).
3. The user enters their height in centimeters.
4. The height value is converted from centimeters to meters.
5. BMI is calculated using the formula:

BMI = weight / (height²)

6. The calculated BMI value is evaluated using conditional statements.
7. The program prints the BMI value and a corresponding health category.

---

## 🧠 BMI Classification Logic

- BMI < 18.5 → Underweight
- 18.5 ≤ BMI ≤ 24.9 → Normal
- 25 ≤ BMI ≤ 29.9 → Overweight
- BMI ≥ 30 → Obese

Each category includes a short recommendation message for the user.

---

## 💡 Sample Output

---BMI HESAPLAYICI---
Kilonuzu (kg) giriniz: 70
Boyunuzu (cm) giriniz: 175

Vücut kitle indexiniz: 22.86, NORMAL
Gayet normal kilodasınız.

---

## 🧩 Concepts Used

- User input with input()
- Type conversion using float
- Mathematical operations and pow()
- Conditional statements (if / elif / else)
- Basic input validation
- Formatted output with f-strings

---

## 📄 Project Structure

python-projects/
└── BMICalculator/
    ├── bmi_calculator.py
    └── README.md

---

## ▶️ How to Run

1. Copy or download the project files.
2. Open a terminal in the project directory.
3. Run the program using the following command:

python bmi_calculator.py

4. Follow the instructions displayed in the console.

---

This project is suitable for beginners who want to strengthen their Python fundamentals while building a practical, real-world console application.
