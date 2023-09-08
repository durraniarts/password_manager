from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)


    password_entry.delete(0,END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def _save():
    website_name = website_entry.get()
    username = username_entry.get()
    _password = password_entry.get()


    if len(website_name) == 0 or len(username) == 0 or len(_password) == 0:
        messagebox.showerror(title='Error', message="Please don't leave any field empty.")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered: \nEmail: {username}\nPassword: {_password}\nIs it ok to save?")
        if is_ok:
            with open('data.txt', mode='a', encoding='utf8') as _f:
                _f.writelines(f"{website_name} | {username} | {_password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# ------------------- canvas to make logo appear on screen -----------------

canvas = Canvas(width=200, height=200)
_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=_image)
canvas.grid(column=1, row=0)

# ------------------------ Labels ------------------

website_label = Label(text='Website:', pady=7)
website_label.grid(column=0, row=1)
username_label = Label(text='Email/Username:', pady=7, padx=10)
username_label.grid(column=0, row=2)
password_label = Label(text='Password:', pady=7)
password_label.grid(column=0, row=3)

# ----------------------- Entries -------------------

website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
username_entry = Entry(width=52)
username_entry.insert(0, 'abdurrehmandurrani1215@gmail.com')
username_entry.grid(column=1, row=2 , columnspan=2)
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# ---------------------------- Buttons -----------------------

generate_button = Button(text='Generate Password', width=15, command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text='Add', width=44, command=_save)
add_button.grid(column=1, row=4, columnspan=2, pady=5)

# ------------------ window main loop to keep updated ---------------------

window.mainloop()
