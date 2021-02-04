
import tkinter
from tkinter import *
import random, string
import pyperclip


root = tkinter.Tk() # calling tkinter
root.geometry('400x600') # Size of Dice
root.title('Password Generator')
intro_label = tkinter.Label(root, text="Password Generator Application", fg = "black",font = "Helvetica 16 bold italic").pack()

length_label = tkinter.Label(root, text="Password Length", fg = "black", font = ('Courier',14,'bold','italic')).pack()
pass_len = IntVar()

length_feild = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()

pass_str = StringVar()
def Generator():
    password = ''

    for x in range (0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

button = Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

entry_box = Entry(root , textvariable = pass_str).pack()

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)



root.mainloop()