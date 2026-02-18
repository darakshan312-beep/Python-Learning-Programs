# Python-Learning-Programs
This repository contains my Python learning journey and practice  programs. It includes fundamental to intermediate level concepts along with practical exercises, and mini projects. 

# Week One Tasks

# 📌 1️⃣ ATM Withdraw System

## 🏧 ATM Withdraw System

### 📖 Description

This program simulates a basic ATM withdrawal system. It verifies the user’s PIN and allows withdrawal only if the entered amount is available in the account balance.

### 🧠 How It Works

1. The program sets:

   * Available account balance = 10000
   * Correct PIN = 1234

2. The user is asked to:

   * Enter their PIN
   * Enter the withdrawal amount

3. The program checks:

   * If the PIN is correct → prints **"verified"**
   * If the withdrawal amount is less than or equal to available balance:

     * Prints **"valid amount"**
     * Prints **"transaction successful"**
     * Calculates and displays the updated amount
   * If withdrawal amount is greater than balance:

     * Prints **"invalid amount"**

4. If PIN is incorrect:

   * Prints **"invalid pin"**

### 🎯 Purpose

This program demonstrates:

* Conditional statements (if-else)
* User input handling
* Basic arithmetic operations
* Logical validation

---

# 📌 2️⃣ Membership Discount Program (Bonus.py)

## 💳 Membership Discount Program

### 📖 Description

This program calculates membership discount based on the user’s membership type.

### 🧠 How It Works

1. The program:

   * Greets the user
   * Takes total bill input
   * Takes membership type input

2. There are two membership types:

   * **Premium**
   * **Regular**

3. The program checks:

   * If membership type is **premium** → prints "you got 20% discount"
   * If membership type is **regular** → prints "you got 10% discount"
   * If user enters any other type → prints "invalid membership type"

### 🎯 Purpose

This program demonstrates:

* String comparison
* Conditional statements (if-elif-else)
* Basic user interaction

---

# 📌 3️⃣ Charity Donation Bonus (Charity.py)

## 🎁 Charity Donation Bonus Program

### 📖 Description

This program calculates bonus percentage based on the donation amount entered by the user.

### 🧠 How It Works

1. The program takes donation amount as input.

2. Conditions:

   * Maximum donation threshold = 10000
   * Minimum donation threshold = 5000

3. The program checks:

   * If donation ≥ 10000:

     * Calculates 20% bonus
     * Displays bonus amount

   * If donation is between 5000 and 10000:

     * Calculates 10% bonus
     * Displays bonus amount

   * If donation < 5000:

     * Prints "no bonus for your donation"

4. Bonus is calculated using:

   ```
   bonus = (number / 100 * percentage)
   ```

### 🎯 Purpose

This program demonstrates:

* Conditional logic
* Percentage calculation
* Arithmetic operations
* Multiple condition checking using elif

