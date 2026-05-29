# 🏦 Banking Management System (Python + MySQL)

## 📌 Overview
This is a simple **Banking Management System** built using **Python and MySQL**.
It is a command-line project that allows users to perform basic banking operations such as creating accounts, depositing money, withdrawing money, and checking balances.

This project is designed for learning database integration with Python.

---

## ⚙️ Features
- Create new bank account
- View account details
- Deposit money
- Withdraw money
- Check account balance
- Delete account (if implemented)

---

## 🛠️ Technologies Used
- Python 3
- MySQL Database
- mysql-connector-python
- VS Code (development environment)
- Virtual Environment (venv)

---

## 📂 Project Structure
Banking-System/
│
├── main.py
├── database/
├── venv/
├── requirements.txt
├── README.md
└── (other python files)

## Create Virtual environment
python -m venv venv

## Activate Virtual environment
- Windows
venv\Scripts\activate

## Install dependencies
pip install -r requirements.txt

## Setup MySQL database
--Create Database
DROP DATABASE banking_system IF EXISTS;
CREATE DATABASE banking_system;

--Create tables
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    surname VARCHAR(100),
    email VARCHAR(100)
);

## How to run the project
python main.py

## Requirements
mysql-connector-python
python-dotenv
rich

## Learning outcomes
- Python MySQL connection
- CRUD operations
- Database handling
- CLI application structure

## Author
Bonolo Lekalakala