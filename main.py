from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip

FONT = ("Segoe UI", 12)
DATA_FILE = "credentials.txt"

# -------------------------- PASSWORD CREATOR -------------------------- #
def create_strong_password():
    """
    Generates a secure random password using letters, digits, and symbols.
    Copies it to the clipboard automatically.
    """
    characters = string.ascii_letters + string.digits + "!#$%&()*+"
    password = ''.join(random.choice(characters) for _ in range(random.randint(12, 16)))
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE ENTRY ----------------------------- #
def save_credentials():
    """
    Saves the credentials entered by the user to a local file after validation.
    """
    website = website_input.get().strip()
    email = email_input.get().strip()
    password = password_input.get().strip()

    if not website or not password:
        messagebox.showwarning(title="Input Error", message="Website and Password fields cannot be empty.")
        return

    confirm = messagebox.askokcancel(title="Confirm Entry", 
                                     message=f"Save the following details?\n\nWebsite: {website}\nEmail: {email}\nPassword: {password}")
    if confirm:
        with open(DATA_FILE, "a") as file:
            file.write(f"{website} | {email} | {password}\n")
        website_input.delete(0, END)
        password_input.delete(0, END)
        messagebox.showinfo(title="Success", message="Credentials saved successfully!")

# ----------------------------- UI DESIGN ----------------------------- #
window = Tk()
window.title("SecurePass - Password Vault")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")  # Make sure your logo.png exists in the folder
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Website
Label(text="Website:", font=FONT).grid(row=1, column=0)
website_input = Entry(width=36)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

# Email
Label(text="Email/Username:", font=FONT).grid(row=2, column=0)
email_input = Entry(width=36)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "aqil.rasheed2002@gmail.com")

# Password
Label(text="Password:", font=FONT).grid(row=3, column=0)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

Button(text="Generate", command=create_strong_password).grid(row=3, column=2)

# Add button
Button(text="Save", width=36, command=save_credentials).grid(row=4, column=1, columnspan=2)

window.mainloop()
