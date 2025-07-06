# 🎮 Number Guessing Game (Computer Guesses)

A fun terminal-based Python game where the **computer tries to guess your number**! You think of a number, set a maximum range, and give the computer feedback after each guess. The goal is for the computer to figure out your number as efficiently as possible.

---

## 🧠 How It Works

1. **You set the max range** by entering the highest possible number.
2. **You secretly think of a number** between 1 and your chosen max.
3. The computer guesses a number.
4. You respond with:
   - `'h'` if the guess is too **high**
   - `'l'` if the guess is too **low**
   - `'c'` if the guess is **correct**
5. The computer narrows down the range based on your feedback and keeps guessing until it gets it right.
6. After each round, you’ll be asked if you want to **play again**.

---


## 📦 Features

- 🧮 Tracks number of attempts
- 🧠 Binary search-style guessing
- 🛑 Detects contradictory user feedback
- 🔁 Option to restart the game after each round
- 🚫 Handles invalid inputs gracefully

---

## 🛠️ Requirements

- Python 3.x

No external libraries are required — just run it in any terminal with Python installed.

---

## 🚀 Getting Started