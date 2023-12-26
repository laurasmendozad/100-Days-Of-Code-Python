''' Password Generator GUI Application '''
from tkinter import *
from random import randint, choice, shuffle
from tkinter import messagebox
import pyperclip
import json
# -------------------------------------- PASSWORD GENERATOR -------------------------------------- #

def generate_password():
    ''' Function to Generate the Password '''
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
               'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for i in range(0,randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(0,randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(0,randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ----------------------------------------- SAVE PASSWORD ---------------------------------------- #

def save_password():
    '''Function to Actualize Password File'''

    new_data = {
        website_entry.get(): {
            "email": user_entry.get(),
            "password": password_entry.get()
        }
    }

    if len(website_entry.get())==0 or len(user_entry.get())==0 or len(password_entry.get())==0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("ProjectsPerDay\Day 030\Project - Password Manager Part 2\data.json", "r", encoding="utf-8") as pass_file:
                # Read old data
                data = json.load(pass_file)
                # Updating old data with new data
                data.update(new_data)

        except FileNotFoundError:
            data = new_data

        finally:
            with open("ProjectsPerDay\Day 030\Project - Password Manager Part 2\data.json", "w", encoding="utf-8") as pass_file:
                # Saving updated data
                json.dump(data, pass_file, indent=4)

            website_entry.delete(0, END)
            user_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

# ----------------------------------------- FIND PASSWORD ---------------------------------------- #

def find_password():
    ''' Function to Search an Specific Password '''
    website = website_entry.get()
    try:
        with open("ProjectsPerDay\Day 030\Project - Password Manager Part 2\data.json", "r", encoding="utf-8") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists")

# ------------------------------------------- UI SETUP ------------------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="ProjectsPerDay\Day 030\Project - Password Manager Part 2\logo.png")
canvas.create_image(100, 100, image = img)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website:", anchor="e", width=13)
website_label.grid(row=1, column=0)

user_label = Label(text="Email/Username:", anchor="e", width=13)
user_label.grid(row=2, column=0)

password_label = Label(text="Password:", anchor="e", width=13)
password_label.grid(row=3, column=0)

# Entries

website_entry = Entry(width=32)
website_entry.grid(row=1, column=1)
website_entry.focus()

user_entry = Entry(width=50)
user_entry.grid(row=2, column=1, columnspan=2)
# user_entry.insert(0,"username@email.com")

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

gen_pass_button = Button(text="Generate Password", width=14, command=generate_password)
gen_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=42, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
