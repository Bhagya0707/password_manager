from tkinter import *
import random
import string

def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for i in range(12))
    entry_password.delete(0, END)
    entry_password.insert(0, password)

def save_password():
    website = entry_website.get()
    password = entry_password.get()
    with open("passwords.txt", "a") as f:
        f.write(f"{website} : {password}\n")
    print(f"Saved password for {website}")

root = Tk()
root.title("Password Manager")
root.geometry("400x300")

Label(root, text="Website").pack()
entry_website = Entry(root)
entry_website.pack()

Label(root, text="Password").pack()
entry_password = Entry(root)
entry_password.pack()

Button(root, text="Generate Password", command=generate_password).pack(pady=5)
Button(root, text="Save Password", command=save_password).pack(pady=5)

root.mainloop()
