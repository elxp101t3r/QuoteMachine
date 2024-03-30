from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *
import requests as re


response = re.get(url='https://zenquotes.io/api/today')
data = response.json()
quote = data[0]['q']

        

window = Tk()
window.geometry('1200x600')
title = Label(
    text='Quote Machine',
    bootstyle='success',
    font=('Arial', 40, 'bold')
)
title.grid(row=0, column=1)

quote = Label(bootstyle='inverse-dark', text=f'{quote}', font=('Verdana', 15, 'bold', 'italic'))

quote.grid(row=1, column=1)

window.mainloop()