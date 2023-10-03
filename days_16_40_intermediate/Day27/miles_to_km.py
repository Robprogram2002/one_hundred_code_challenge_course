from tkinter import *

window = Tk()
window.title("Mile to km Converter")
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=1, row=0)

mile_text = Label(text="Miles", font=("Arial", 16))
mile_text.grid(column=2, row=0)
mile_text.config(padx=10)

equal_text = Label(text="is equal to", font=("Arial", 16))
equal_text.grid(column=0, row=1)

result = Label(text="")
result.grid(column=1, row=1)

km_text = Label(text="Km", font=("Arial", 16))
km_text.grid(column=2, row=1)
km_text.config(padx=10)


def button_clicked():
    miles = float(input.get())
    km = miles * 1.689
    result.config(text=f"{km}")


# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
