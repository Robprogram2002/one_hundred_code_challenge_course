from tkinter import *
from tkinter import messagebox
from generate_password import generate_password
import pyperclip

BG = "white"
WIDTH = 35
SHORT_WIDTH = 21


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def handle_password():
    if password.get() != "":
        password.delete(0, END)

    new_password = generate_password()
    password.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def reset_entries():
    website.delete(0, END)
    user.delete(0, END)
    user.insert(0, get_common_user())
    password.delete(0, END)
    website.focus()


def add_password():
    web_info = website.get()
    user_info = user.get()
    pass_info = password.get()

    if web_info == "" or user_info == "" or pass_info == "":
        messagebox.showinfo(title="Ooops", message="Please, make sure you haven't left any fields empty.")
        return

    confirmation = messagebox.askokcancel(title=web_info,
                                          message=f"These are the details entered: \nEmail: {user_info} \nPassword: "
                                                  f"{pass_info} \nIt's ok to save ? ")

    if confirmation:
        with open("data.txt", mode="a") as file:
            new = f"{web_info} | {user_info} | {pass_info} \n"
            file.write(new)

        reset_entries()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# website entry
web_label = Label(text="Website :")
web_label.grid(column=0, row=1)
web_label.config(pady=2)

website = Entry(width=WIDTH)
website.grid(column=1, row=1, columnspan=2)
website.focus()


def get_common_user():
    with open("data.txt") as file:
        lines = file.readlines()
        users = [l.split("|")[1].strip() for l in lines]
        freq = {}
        for u in users:
            if u in freq:
                freq[u] += 1
            else:
                freq[u] = 1
        max_val = 0
        max_name = ""
        for k in freq.keys():
            if freq[k] > max_val:
                max_val = freq[k]
                max_name = k
        return max_name


# user entry
user_label = Label(text="Email/Username :")
user_label.grid(column=0, row=2)
user_label.config(pady=2)

user = Entry(width=WIDTH)
user.insert(0, get_common_user())
user.grid(column=1, row=2, columnspan=2)

# password entry
password_label = Label(text="Password :", )
password_label.grid(column=0, row=3)
password_label.config(pady=2)

password = Entry(width=SHORT_WIDTH)
password.grid(column=1, row=3)

play_button = Button(text="Generate Password", command=handle_password)
play_button.grid(column=2, row=3)

add_button = Button(text="Add", width=WIDTH + 1, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
