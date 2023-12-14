''' Taylor Quotes '''
from tkinter import *
import requests
import json

def get_quote():
    ''' Get Quote from API '''
    r = requests.get(url='https://taylorswiftapi.onrender.com/get')
    canvas.itemconfig(quote_text, text=r.json()["quote"])


window = Tk()
window.title("Taylor Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207,
                                text="Taylor Quote Goes HERE",
                                width=250,
                                font=("Arial", 15, "bold"),
                                justify= CENTER,
                                fill="white")
canvas.grid(row=0, column=0)

taylor_img = PhotoImage(file="taylor.png")
taylor_button = Button(image=taylor_img, highlightthickness=0, command=get_quote)
taylor_button.grid(row=1, column=0)

window.mainloop()
