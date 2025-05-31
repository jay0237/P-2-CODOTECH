import tkinter as tk
from tkinter import messagebox
import string
import secrets
import pyperclip  # Make sure pyperclip is installed



def generate_password():
    length = int(length_entry.get())
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digit_var.get()
    use_special = special_var.get()

    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Select at least one character type.")
        return

    password = ''.join(secrets.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.pack()

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase", variable=upper_var).pack()
tk.Checkbutton(root, text="Include Lowercase", variable=lower_var).pack()
tk.Checkbutton(root, text="Include Digits", variable=digit_var).pack()
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Helvetica", 12), justify="center", state="readonly").pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

root.mainloop()
