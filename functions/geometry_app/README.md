# 📐 Geometry App — Geometric Area Calculator (Python)

This project is a **menu-driven Python console application** that calculates the areas of various geometric shapes using **separate functions**.  
Each geometric calculation is implemented as an independent function, allowing the program to be modular, readable, and reusable.

The application continuously runs until the user chooses to exit and includes input validation to prevent invalid data entry.

---

## 🎯 Purpose of This Project

- Practice defining and using **functions** in Python  
- Separate calculation logic from program flow  
- Reinforce mathematical formula implementation  
- Build a clean, menu-based console application  
- Improve error handling with `try–except`  

---

## 📌 Supported Shapes & Calculations

The application can calculate the area of the following shapes:

- **Circle**  
- **Square**  
- **Rectangle** (with short–long side validation)  
- **Triangle**  
- **Cylinder (surface area)**  

Each calculation is handled by its own function.

---

## 🧠 Implemented Functions

- `daire_alan(r)` → Calculates circle area  
- `kare_alan(kenar)` → Calculates square area  
- `dikdortgen_alan(kisa_kenar, uzun_kenar)` → Calculates rectangle area  
- `ucgen_alan(kenar, yukseklik)` → Calculates triangle area  
- `silindir_alan(yaricap, yukseklik)` → Calculates cylinder surface area  

The `math` module is used for precise calculations involving π and powers.

---

## 🧠 Python Concepts Practiced

- Function definitions and return values  
- Parameter passing  
- Menu-based program design  
- Infinite loops (`while True`)  
- Input validation and logical checks  
- Exception handling with `try–except`  
- Mathematical operations using the `math` module  

---

## 🖥 Sample Program Flow

=== Geometric Shape Area Calculator ===  

1. Circle area  
2. Square area  
3. Rectangle area  
4. Triangle area  
5. Cylinder area  
6. Exit  

Selection: 1  
Enter radius: 5  
Circle area: 78.54  

Selection: 6  
Exited successfully.

---

## 📂 Folder Structure

functions/  
└── geometry_app/  
    ├── main.py  
    └── README.md  

---

## 🚀 How to Run

1. Navigate to the `geometry_app` directory  
2. Run the application using Python:
   python main.py  
3. Select a shape from the menu and enter the required values  

---

## 🎯 Learning Outcome

This project demonstrates how **functions** can be used to organize code efficiently in Python.  
By isolating each geometric calculation into its own function, the program becomes easier to read, maintain, and extend.

---
