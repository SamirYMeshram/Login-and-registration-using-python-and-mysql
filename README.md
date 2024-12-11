# **🔐 Login and Registration System**  

## **📖 Overview**  
The **Login and Registration System** is a secure, user-friendly system developed in **Python** with a **MySQL** database. It allows users to register by creating an account with a unique username and password. Once registered, users can log in to access their personalized dashboard.  

This system features robust error handling, data validation, and password encryption to ensure security and data privacy. It also includes a modern, user-friendly interface built using **Tkinter**.  

The system can be used as a standalone project or integrated into larger web or desktop applications that require user authentication and authorization.  

---

## **✨ Key Features**  
- **User Registration**: Create new accounts with unique usernames and passwords.  
- **Secure Login**: Login with a registered username and password.  
- **Data Validation**: Ensures that users enter valid data during registration and login.  
- **Password Encryption**: Uses **bcrypt** to encrypt passwords before storing them in the database.  
- **Interactive GUI**: A clean, user-friendly graphical user interface (GUI) built with **Tkinter**.  
- **Error Handling**: Handles invalid input, duplicate usernames, and system errors gracefully.  

---

## **🛠️ Technologies Used**  
- **Python**: Main programming language used for logic and GUI.  
- **MySQL**: Relational database used for user data storage.  
- **Tkinter**: Library for building the graphical user interface (GUI).  
- **bcrypt**: Library for hashing and verifying passwords.  

---

## **📁 Folder Structure**  
```
📦 Login-and-Registration-System  
├── 📄 main.py              # Main Python script with login, registration, and GUI logic  
├── 📄 database.sql         # SQL file to create the necessary database and table  
├── 📄 requirements.txt     # Required libraries for the project  
└── 📄 README.md            # Project documentation (this file)  
```

---

## 📸 **Screenshots**  
> **Add screenshots of the user interface for registration, login, and dashboard.**  

---

## ⚙️ **Installation and Setup**  
Follow the steps below to set up the **Login and Registration System** on your system.  

---

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/Login-and-Registration-System.git
cd Login-and-Registration-System
```

---

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**  
```bash
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate     # For Windows
```

---

### **3️⃣ Install Required Libraries**  
Install all the dependencies listed in `requirements.txt` using:  
```bash
pip install -r requirements.txt
```

---

### **4️⃣ Set Up the MySQL Database**  
To set up the **MySQL database**, follow these steps:  

#### **Option 1: Using SQL Script**  
1. **Open MySQL Workbench** or any MySQL database client.  
2. Run the SQL script in **`database.sql`**. This will create the database and users table.  

```sql
CREATE DATABASE login_system;

USE login_system;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

#### **Option 2: Manually Create the Database and Table**  
If you do not want to use the SQL script, follow these steps manually:  

1. **Open MySQL Workbench** or **phpMyAdmin**.  
2. **Create a New Database**:  
   ```sql
   CREATE DATABASE login_system;
   ```

3. **Use the Database**:  
   ```sql
   USE login_system;
   ```

4. **Create the Users Table**:  
   ```sql
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) NOT NULL UNIQUE,
       password VARCHAR(255) NOT NULL
   );
   ```

5. **Verify the Table**:  
   Run the following command to ensure the table has been created:  
   ```sql
   SHOW TABLES;
   ```

---

### **5️⃣ Update MySQL Connection Details in `main.py`**  
In **main.py**, update the MySQL connection details as shown below:  
```python
db = mysql.connector.connect(
    host="localhost",           # Change this if MySQL is on a different server
    user="your_username",       # Replace with your MySQL username
    password="your_password",   # Replace with your MySQL password
    database="login_system"     # This should match the name of your database
)
```

---

### **6️⃣ Run the Application**  
Run the following command to launch the application:  
```bash
python main.py
```

If everything is set up correctly, the login and registration window will open. You can register and log in to access your dashboard.  

---

## 📚 **How to Use the Application**  
1. **Launch the Application**: Run `main.py` to open the login and registration system.  
2. **Register**: Click on the **Register** button to create a new account. Enter a unique username and password.  
3. **Login**: After registration, use the same username and password to log in.  
4. **Dashboard**: After logging in, you'll see a simple **welcome message**.  

---

## 📋 **Requirements**  
To run the application, you’ll need the following libraries:  

```
tkinter
mysql-connector-python
bcrypt
```

To install all the dependencies, use:  
```bash
pip install -r requirements.txt
```

---

## 📋 **Troubleshooting**  
**Issue**: MySQL connection failed.  
**Solution**: Ensure your MySQL server is running. Verify your **host**, **username**, **password**, and **database** details in **main.py**.  

**Issue**: Username already exists.  
**Solution**: Choose a different, unique username.  

**Issue**: Cannot log in with valid credentials.  
**Solution**: Check if the password was entered correctly and if the database is properly connected.  

---

## 🔮 **Possible Enhancements**  
- **Forgot Password**: Add a "Forgot Password" feature to allow users to reset their password.  
- **Admin Dashboard**: Allow administrators to manage user accounts.  
- **Email Verification**: Add email verification before activating user accounts.  
- **Captcha Verification**: Add CAPTCHA to prevent bots from registering multiple accounts.  

---

## 💻 **Code Explanation**  

### **main.py**  
This file contains all the core logic, including MySQL connection, user registration, user login, and GUI creation.  

### **Key Functions**  
| **Function**               | **Description**                                             |
|-------------------------- |---------------------------------------------------------- |
| `register_user()`           | Handles the user registration process.                    |
| `login_user()`              | Handles the user login process.                           |
| `hash_password(password)`   | Hashes the user's password using **bcrypt**.               |
| `check_username_exists()`   | Checks if the username is already registered in the database. |
| `create_user()`             | Creates a new user account and stores it in the database.  |
| `validate_inputs()`         | Validates the username and password inputs.               |
| `connect_to_database()`     | Establishes a connection to the MySQL database.           |

---

## 🤝 **Contributing**  
Contributions are welcome! To contribute:  
1. Fork the repository.  
2. Create a new feature branch (`git checkout -b feature-name`).  
3. Make changes, then commit (`git commit -m "Added new feature"`).  
4. Push to your branch (`git push origin feature-name`).  
5. Open a pull request and describe your changes.  

---

## 📝 **License**  
This project is licensed under the **MIT License**. See the `LICENSE` file for more details.  

---

## 👤 **Author**  
- **Name**: Samir Y Meshram  
- **GitHub**: [SamirYMeshram](https://github.com/SamirYMeshram)  
- **Email**: sameerYmeshram@gmail.com  

---

