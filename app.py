import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import hashlib
from ttkthemes import ThemedTk


# --- Database configuration ---
db_config = {
    'host': 'localhost',
    'user': 'your_db_user',  # Replace with your MySQL username
    'password': 'your_db_password',  # Replace with your MySQL password
    'database': 'user_system' # Replace with your database name
}

def connect_to_db():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

# --- User functions (Database interaction)---

def register_user():
    username = entry_username_reg.get().strip()
    password = entry_password_reg.get().strip()

    if not username or not password:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    connection = connect_to_db()
    if connection is None:
        return

    cursor = connection.cursor()
    try:
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, hashed_password))
        connection.commit()
        messagebox.showinfo("Success", "Registration successful!")
        entry_username_reg.delete(0, tk.END)
        entry_password_reg.delete(0, tk.END)

        show_login_frame() # Automatically switch to login after successful registration


    except mysql.connector.Error as err:
        if err.errno == 1062: # Duplicate entry error (username already exists)
            messagebox.showerror("Error", "Username already exists. Please choose another.")

        else:
           messagebox.showerror("Error", f"Error: {err}")

    finally:
        cursor.close()
        connection.close()




def login_user():
    username = entry_username_login.get().strip()
    password = entry_password_login.get().strip()

    if not username or not password:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    connection = connect_to_db()
    if connection is None:
        return

    cursor = connection.cursor()
    try:
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, hashed_password))
        user = cursor.fetchone()


        if user:
            messagebox.showinfo("Login Success", f"Welcome, {username}!")
            entry_username_login.delete(0, tk.END)
            entry_password_login.delete(0, tk.END)

        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")


    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")  # Handle other DB errors

    finally:
        cursor.close()
        connection.close()




# --- Main UI ---

root = ThemedTk(theme="arc")
root.title("Login & Registration")
root.geometry("450x550")
root.resizable(False, False)

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 14), padding=(10, 5))
style.configure("TEntry", font=("Helvetica", 12))


# Frame switching functions

def show_frame(frame):
    frame.grid(row=0, column=0, sticky="nsew")

def show_register_frame():
    frame_login.grid_forget()
    show_frame(frame_register)


def show_login_frame():
    frame_register.grid_forget()
    show_frame(frame_login)




# --- Frames ---
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame_login = ttk.Frame(root)
frame_register = ttk.Frame(root)


# --- Styling functions (can be further customized) ---

def style_button(button, style_name="TButton"):
    button.configure(style=style_name)

def create_styled_button(parent, text, command, style_name="TButton", **kwargs):
    button = ttk.Button(parent, text=text, command=command, style=style_name, **kwargs)
    return button


style.configure("Accent.TButton", foreground="white", background="#3498db")
style.map("Accent.TButton", background=[("active", "#2980b9")])  # Hover

style.configure("Success.TButton", foreground="white", background="#2ecc71")
style.map("Success.TButton", background=[("active", "#27ae60")])  # Hover


# --- Login Frame widgets ---

ttk.Label(frame_login, text="Login", font=("Helvetica", 28, "bold")).grid(row=0, column=0, pady=(40, 20), columnspan=2)

ttk.Label(frame_login, text="Username").grid(row=1, column=0, sticky=tk.W, padx=20)
entry_username_login = ttk.Entry(frame_login)
entry_username_login.grid(row=1, column=1, pady=10, padx=(0,20), sticky=tk.E)



ttk.Label(frame_login, text="Password").grid(row=2, column=0, sticky=tk.W, padx=20)
entry_password_login = ttk.Entry(frame_login, show="*")
entry_password_login.grid(row=2, column=1, pady=10, padx=(0,20), sticky=tk.E)

btn_login = create_styled_button(frame_login, text="Login", command=login_user, style_name="Accent.TButton")
btn_login.grid(row=3, column=0, columnspan=2, pady=20)

btn_to_register = create_styled_button(frame_login, text="Don't have an account? Register", command=show_register_frame, style_name="Success.TButton")
btn_to_register.grid(row=4, column=0, columnspan=2)



# --- Registration Frame widgets ---
ttk.Label(frame_register, text="Register", font=("Helvetica", 28, "bold")).grid(row=0, column=0, pady=(40, 20), columnspan=2)


ttk.Label(frame_register, text="Username").grid(row=1, column=0, sticky=tk.W, padx=20)
entry_username_reg = ttk.Entry(frame_register) # ttk entry for register username
entry_username_reg.grid(row=1, column=1, pady=10, padx=(0,20), sticky=tk.E)

ttk.Label(frame_register, text="Password").grid(row=2, column=0, sticky=tk.W, padx=20)
entry_password_reg = ttk.Entry(frame_register, show="*")  # ttk entry for register password
entry_password_reg.grid(row=2, column=1, pady=10, padx=(0,20), sticky=tk.E)

btn_register = create_styled_button(frame_register, text="Register", command=register_user, style_name="Accent.TButton")
btn_register.grid(row=3, column=0, columnspan=2, pady=20)  # moved register button up


btn_to_login = create_styled_button(frame_register, text="Already have an account? Login", command=show_login_frame, style_name="Success.TButton")
btn_to_login.grid(row=4, column=0, columnspan=2)  # moved login button up





show_login_frame()  # Show login frame initially

root.mainloop()
