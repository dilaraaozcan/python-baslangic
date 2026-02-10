# ⚡ Electricity Bill Calculator — Python Console Application

This project is a **Python console-based application** that calculates an electricity bill based on daily consumption data entered by the user.  
The program analyzes total and average consumption, determines the consumption tier, and calculates the final bill accordingly.

It is designed as a mini project to practice **lists**, **loops**, **conditional logic**, and **match–case** usage together.

---

## 🎯 Purpose of This Project

- Practice collecting and storing numerical data in a list  
- Analyze total and average electricity consumption  
- Apply tier-based (kademeli) billing logic  
- Use both `if–elif–else` and `match–case` structures  
- Build a complete, interactive console application  

---

## ⚙️ Program Features

- Takes the number of billing days as input  
- Collects daily electricity consumption values  
- Stores consumption data in a list  
- Calculates:
  - Total electricity consumption  
  - Average daily consumption  
- Determines consumption tier:
  - **Low** (Below 150 units)  
  - **Medium** (150–300 units)  
  - **High** (Above 300 units)  
- Calculates the final bill based on the tier:
  - Low → 1.5 TL per unit  
  - Medium → 2.2 TL per unit  
  - High → 3.0 TL per unit  

---

## 🧠 Python Concepts Practiced

- Lists and list iteration  
- `while` and `for` loops  
- Accumulator variables  
- Conditional logic (`if`, `elif`, `else`)  
- `match–case` decision structure  
- Numeric calculations  
- Console input/output  

---

## 🖥 Sample Program Output

=== ELECTRICITY BILL CALCULATOR ===  

How many days will be calculated? 3  

1st day consumption: 60  
2nd day consumption: 55  
3rd day consumption: 70  

Total consumption: 185 units  
Average daily consumption: 61.67  

--- Tier Calculation ---  
Tier: Medium  
Total bill amount: 407.0 TL  

---

## 📂 Folder Structure

mini-projects/  
└── electricity_bill_calculator/  
    ├── main.py  
    └── README.md  

---

## 🚀 How to Run

1. Navigate to the `electricity_bill_calculator` folder  
2. Run the program using Python:
   python main.py  
3. Enter daily consumption values as prompted  

---

## 🎯 Learning Outcome

This project demonstrates how **real-world billing logic** can be modeled using Python.  
It strengthens skills in data collection, list-based analysis, conditional branching, and structured decision-making.

---