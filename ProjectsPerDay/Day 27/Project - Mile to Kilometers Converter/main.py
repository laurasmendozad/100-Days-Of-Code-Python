''' Mile to Kilometer Converter Project '''
from tkinter import *

def button_clicked():
    ''' Do when the button is clicked '''
    mile = float(entry.get())
    km = round(mile * 1.609,2)
    label2.config(text=str(km))

FONT = ("Arial", 12)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)

entry = Entry(width=10)
entry.grid(column=1, row=0)

label0 = Label(text="Miles", font=FONT)
label0.grid(column=2, row=0)

label1 = Label(text="is equal to", font=FONT)
label1.grid(column=0, row=1)

label2 = Label(text="0", font=FONT)
label2.grid(column=1, row=1)

label3 = Label(text="Km", font=FONT)
label3.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked, font=FONT)
button.grid(column=1, row=2)

window.mainloop()
