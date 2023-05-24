import os
import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    capital_letter = random.choice(string.ascii_uppercase)
    special_chars = random.sample(string.punctuation, 2)
    alphanumeric = string.ascii_letters + string.digits
    rem_chars = ''.join(random.choice(alphanumeric) for _ in range(5))
    password = capital_letter + special_chars[0] + special_chars[1] + rem_chars
    password_lst = list(password)
    random.SystemRandom().shuffle(password_lst)
    password = ''.join(password_lst)
    return password

def save_password():
    identify = entry_identify.get()
    if identify:
        password = generate_password()
        file_path = f"{identify}.txt"
        with open(file_path, 'w') as file:
            file.write(password)
        messagebox.showinfo("Password Saved", f"Find your password for {identify} at:\n{os.path.join(os.getcwd(), file_path)}")
    else:
        messagebox.showwarning("Identification Required", "Please enter an identification for the password.")

# Create the main window
window = tk.Tk()
window.title("Pass_gen")
window.geometry("230x90")

# Create the identification label and entry
label_identify = tk.Label(window, text="Identification:")
label_identify.pack()
entry_identify = tk.Entry(window)
entry_identify.pack()

# Create the generate password button
btn_generate = tk.Button(window, text="Generate Password", command=save_password)
btn_generate.pack()

# Start the main event loop
window.mainloop()
