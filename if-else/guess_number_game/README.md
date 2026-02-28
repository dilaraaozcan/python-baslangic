# 🎯 Guess Number Game — Python Console Application

This project is a console-based number guessing game developed in Python.  
The player tries to guess a randomly generated number between **1 and 100** within a limited number of attempts. The system also tracks successful game scores (number of attempts) and displays a sorted leaderboard.

This project is located in:

python-baslangic/  
└── if-else/  
    └── guess_number_game/  
        ├── main.py  
        └── README.md  

---

## 🎯 Project Purpose

- Practice `if-else` conditional structures in real gameplay decisions  
- Strengthen loop logic (`while`) with attempt-limited gameplay  
- Use random number generation for dynamic game behavior  
- Track and sort scores using lists  
- Validate user input with `try-except`  
- Build a menu-driven interactive console application  

---

## 🧩 Features

- Menu system:
  1. Play  
  2. Scores  
  3. Exit  

- Random target number generation: `random.randint(1, 100)`  
- 10 attempts per game session  
- Guidance messages:
  - Guess is too low → prompts for a higher number  
  - Guess is too high → prompts for a lower number  
- Score tracking:
  - Saves attempt count when the player guesses correctly  
  - Sorts scores from best to worst  
- Input validation:
  - Prevents crashes when non-integer input is entered  

---

## 🎮 Gameplay Rules

- The system selects a random number between **1 and 100**
- The player has **10 total attempts**
- Each guess reduces the remaining attempts
- If the player finds the correct number:
  - The attempt count is recorded
  - The game ends successfully
- If attempts reach 0:
  - The correct number is displayed

---

## 🏆 Scoreboard

- Scores represent the number of attempts used to win
- Lower attempts = better score
- Scores are stored in a list and displayed sorted

Example output:

--- EN İYİ SKORLAR ---  
1. Oyun: 3 deneme  
2. Oyun: 6 deneme  

---

## 🧠 Concepts Practiced

- `if-elif-else` decision structures  
- Nested `while` loops  
- Random number generation  
- List operations (`append`, `sort`)  
- Menu-based program flow  
- Exception handling (`try-except`)  
- Basic game state tracking (attempts, tries, scores)  

---

## ▶️ How to Run

From the project folder:

python main.py

Follow the on-screen menu to play or view scores.

---

## 🚀 Why This Project Matters

This project is a clean example of combining conditionals + loops to build an interactive console game.  
It also introduces a simple leaderboard system and reinforces defensive programming with input validation.

---
