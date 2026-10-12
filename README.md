# 🏦 Bank Management System

An interactive bank management web application built with Python and Streamlit to demonstrate basic banking operations through a user-friendly interface.

## 🌐 Live Demo

🚀 **Try the application:**  
[Bank Management System — Live Demo](https://bank-management-system-9cnqkza4s3qtvz48mhesb4.streamlit.app/)

📂 **GitHub Repository:**  
[Bank Management System — Source Code](https://github.com/Lokeshcode81/bank-management-system)

## 📌 Project Overview

The Bank Management System is a Python-based project that demonstrates how basic banking operations can be implemented using Object-Oriented Programming (OOP) and Streamlit.

Users can create demo accounts, deposit and withdraw amounts, view account details, update account information, and delete demo accounts through an interactive web interface.

The application uses Streamlit Session State to maintain temporary account data during the active session. It is designed for learning and portfolio demonstration purposes, not for real banking transactions.

## ✨ Key Features

- 🆕 **Create Account** — Create a demo account with basic user details.
- 💰 **Deposit Money** — Add an amount to an existing demo account.
- 💸 **Withdraw Money** — Withdraw funds when sufficient balance is available.
- 🔍 **Show Account Details** — View account information after verification.
- ✏️ **Update Information** — Update account details or PIN.
- 🗑️ **Delete Account** — Remove a demo account from the current session.
- 🔐 **PIN Verification** — Verify account credentials for supported operations.
- ⚡ **Interactive Interface** — Use banking operations through Streamlit.
- ☁️ **Live Deployment** — Access the application online through Streamlit Community Cloud.
- 🧠 **Session-Based Storage** — Maintain temporary data without using a JSON file.

## 🛠️ Technologies Used

- **Python** — Core application logic
- **Streamlit** — Interactive web application interface
- **Object-Oriented Programming (OOP)** — Organizing banking operations using a class
- **Streamlit Session State** — Managing temporary session data
- **Git and GitHub** — Version control and source code hosting
- **Streamlit Community Cloud** — Application deployment

## ⚙️ Application Workflow

1. Open the live application.
2. Select a banking operation from the sidebar.
3. Create a demo account or enter existing account credentials.
4. Perform the selected operation, such as depositing or withdrawing an amount.
5. View the operation status and updated account information.
6. Continue using other operations during the active session.

## 💻 Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Lokeshcode81/bank-management-system.git
```

### 2. Open the Project Folder

```bash
cd bank-management-system
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application should open in your browser. If it does not, use the local URL displayed in the terminal.

**Requirements:** Python and the dependencies listed in `requirements.txt` must be installed.

## 🧪 Banking Operations

| Operation | Description |
|---|---|
| Create Account | Creates a new demo account |
| Deposit | Adds money to the demo account balance |
| Withdraw | Deducts money when sufficient balance is available |
| Show Details | Displays account details without revealing the PIN |
| Update Info | Updates supported account information |
| Delete Account | Deletes the selected demo account |

## 💾 Data Storage

This portfolio version uses **Streamlit Session State** for temporary, session-based data storage.

- No JSON file is required for the deployed Streamlit application.
- Demo account data is not intended to be permanently stored.
- Data may be lost when the session resets or the application restarts.
- The application is not connected to a real banking database.

## 🎓 Key Learning Outcomes

- Applying Object-Oriented Programming in Python
- Building an interactive web application using Streamlit
- Implementing basic account management operations
- Using session state to manage temporary application data
- Adding input validation and account credential checks
- Deploying a Python project online
- Managing and presenting a project on GitHub

## 🚀 Future Improvements

- Add transaction history and account statements
- Integrate a database for persistent storage
- Add automated unit tests
- Improve authentication and account security
- Add transaction summaries and downloadable reports
- Enhance the interface with charts and account activity insights

## ⚠️ Disclaimer

This project is created for educational and portfolio demonstration purposes only. It is **not a real banking application** and must not be used for actual financial transactions or real personal banking information.

Account data is temporary and may be lost. Do not enter real banking credentials or reuse a
