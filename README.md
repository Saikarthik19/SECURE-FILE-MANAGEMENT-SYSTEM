# SECURE-FILE-MANAGEMENT-SYSTEM
A secure file management system with authentication, encryption, and threat detection.
🔐 Secure File Management System

A cybersecurity-based web application that enables users to securely manage files using authentication, encryption, access control, and threat detection features.

🧩 Project Overview

This project aims to create a secure file management platform where users can safely perform file operations like read, write, share, and view metadata. It integrates:

Authentication (password + two-factor)

Encryption (AES for confidentiality)

Access Control (role-based user permissions)

Threat Detection (detects malware & buffer overflow risks)

🚀 Features

✅ Secure Login & Registration ✅ Two-Factor Authentication (OTP) ✅ Role-Based Access Control (Admin/User) ✅ File Upload, Read, Write, and Delete ✅ File Encryption & Decryption ✅ View File Metadata (size, type, date) ✅ Basic Malware Detection ✅ Logging & Console Alerts

🧱 Modules Module Description Authentication Module Manages login, password hashing, and 2FA using OTP. File Management Module Handles secure file operations with encryption and access control. Threat Detection Module Scans uploaded files for malware patterns and risky extensions. ⚙ Tech Stack 💻 Languages & Frameworks

Python 3.10+

Flask (Backend Web Framework)

🧰 Libraries & Tools

flask – Web server framework

flask-login – Authentication handling

pyotp – Two-Factor Authentication (OTP)

cryptography – AES file encryption

sqlite3 – Database for user & file records

hashlib, os – File handling and password hashing

🧑‍💻 Development Tools

VS Code – Code editor

Git & GitHub – Version control

Browser (Chrome/Edge) – For running the Flask app

📂 Folder Structure SecureFileManagementSystem/ │ ├── app/ │ ├── init.py │ ├── auth.py │ ├── routes.py │ ├── models.py │ └── templates/ │ ├── login.html │ ├── dashboard.html │ ├── upload.html │ └── scan_result.html │ ├── static/ │ ├── style.css │ └── script.js │ ├── database/ │ └── sfms.db │ ├── app.py ├── requirements.txt └── README.md

⚡ Installation & Setup 1️⃣ Clone the Repository git clone https://github.com/Pagadalavishnukumar/SecureFileManagementSystem.git cd SecureFileManagementSystem

2️⃣ Create and Activate Virtual Environment python -m venv venv venv\Scripts\activate # On Windows source venv/bin/activate # On macOS/Linux

3️⃣ Install Required Packages pip install flask flask-login pyotp cryptography

4️⃣ Run the Application python app.py

Then open your browser and visit: 👉 http://127.0.0.1:5000

🔄 GitHub Revision Workflow

main branch → stable tested version

feature/auth → authentication module

feature/files → file management module

feature/detection → threat detection module

Example Commands git add . git commit -m "Added AES encryption feature" git push origin feature/files

Merge After Testing git checkout main git merge feature/files git push origin main

🧠 Flow Diagram [User] ↓ [Authentication Module] ↓ [Access Granted] ↓ [File Management Module] ↓ [Threat Detection Module] ↓ [Secure Output]

📈 Future Enhancements

Integrate cloud storage (Azure/AWS)

Add AI-based malware detection

Include real-time user activity monitoring

Provide digital signature verification

🧾 Repository Info

Repository Name: SecureFileManagementSystem GitHub Link: 
🧑‍🎓 Author

Name: Pagadala Vishnu Kumar Institution: Lovely Professional University, CSE- GEN_AI
