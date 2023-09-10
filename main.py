'''Password manager main module'''
import json
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    '''Generates a randomly strong password'''
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
    website_name = website_entry.get().capitalize()
    username = username_entry.get()
    _password = password_entry.get()

    new_data = {
        website_name:{
            'username': username,
            'password': _password
        }
    }

    if len(website_name) == 0 or len(username) == 0 or len(_password) == 0:
        messagebox.showerror(title='Error', message="Please don't leave any field empty.")
    else:
        try:
            with open('data.json', 'r', encoding='utf-8') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print('File created')
            with open('data.json', 'w', encoding='utf-8') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            if website_name in data:
                messagebox.showwarning(message='Website entry already exists')
            else:
                data.update(new_data)
                with open('data.json', 'w', encoding='utf-8') as data_file:
                    json.dump(data, data_file, indent=4)
                    messagebox.showinfo(title=website_name, message='Credentials saved successfully')
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def find_password():
    '''searches the password if exists'''
    website = website_entry.get().capitalize()

    try:
        with open('data.json', 'r', encoding='utf-8') as search_data:
            data = json.load(search_data)
    except FileNotFoundError:
        messagebox.showerror(message='No Data File Found')
    else:
        try:
            username, password = data[website].values()
            messagebox.showinfo(title=website, message=f"Email: {username}\nPassword: {password}")
            pyperclip.copy(password)
        except KeyError:
            messagebox.showerror(message=f'No details for the {website} exists')
    finally:
        website_entry.delete(0, END)

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

website_entry = Entry(width=30)
website_entry.focus()
website_entry.grid(column=1, row=1)
username_entry = Entry(width=52)
username_entry.insert(0, 'abdurrehmandurrani1215@gmail.com')
username_entry.grid(column=1, row=2 , columnspan=2)
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

# ---------------------------- Buttons -----------------------

search_button = Button(text='Search', width=15, command=find_password)
search_button.grid(column=2, row=1, padx=8)
generate_button = Button(text='Generate Password', width=15, command=generate_password)
generate_button.grid(column=2, row=3, padx=8)
add_button = Button(text='Add', width=44, command=_save)
add_button.grid(column=1, row=4, columnspan=2, pady=5)

# ------------------ window main loop to keep updated ---------------------

window.mainloop()
