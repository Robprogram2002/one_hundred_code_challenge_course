import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

data = pandas.read_csv("./data/french_words.csv")
try:
    user_data = pandas.read_csv("./data/user_data.csv")
except FileNotFoundError:
    list_word = data.French.to_list()
    init = {
        "words": list_word,
        "status": [False] * len(list_word)
    }
    user_data = pandas.DataFrame(init)
    user_data.to_csv("./data/user_data.csv", index=False)

index = 0
while user_data.iloc[index].status:
    index += 1


def flip_card(language):
    if language == "French":
        img = front_photo
        color = "black"
    else:
        img = back_photo
        color = "white"

    canvas.itemconfig(card, image=img)
    canvas.itemconfig(title, text=language, fill=color)
    canvas.itemconfig(word, text=f"{data.iloc[index][language]}", fill=color)


turn = window.after(3000, flip_card, "English")


def next_word():
    global turn
    global index
    window.after_cancel(turn)
    index += 1

    while user_data.iloc[index].status:
        index += 1

    canvas.itemconfig(word, text=f"{data.iloc[index].French}")
    flip_card("French")
    turn = window.after(3000, flip_card, "English")


def correct_handler():
    user_data.loc[user_data["words"] == data.iloc[index].French, "status"] = True
    user_data.to_csv("./data/user_data.csv", index=False)

    next_word()


canvas = Canvas(height=525, width=800)
front_photo = PhotoImage(file="./images/card_front.png")
back_photo = PhotoImage(file="./images/card_back.png")

card = canvas.create_image(404, 265, image=front_photo)
title = canvas.create_text(400, 150, text="French", fill="black", font=(FONT_NAME, 40, "italic"))
word = canvas.create_text(400, 263, text=f"{data.iloc[index].French}", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

correct_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
correct_bt = Button(image=correct_img, highlightthickness=0, command=correct_handler)
wrong_bt = Button(image=wrong_img, highlightthickness=0, command=next_word)

correct_bt.grid(column=1, row=1)
wrong_bt.grid(column=0, row=1)

window.mainloop()
