import tkinter
from PIL import Image, ImageTk
import random

# toplevel widget which represents the main window of an application
root = tkinter.Tk() # calling tkinter
root.geometry('400x400') # Size of Dice
root.title('Data Flair Roll the Dice') #set the title of Application

# Adding label into the frame
Label = tkinter.Label(root, text=" ")
Label.pack()

# adding label with different font and formatting
HeadLabel = tkinter.Label(root, text="Let's Begin!", fg = "dark green",
      bg = "light green",
     font = "Helvetica 16 bold italic")
HeadLabel.pack()

# images
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
# simulating the dice with random numbers between 0 to 6 and generating image
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# # construct a label widget for image
Imagelabel = tkinter.Label(root, image=DiceImage)
Imagelabel.image = DiceImage
#
# # packing a widget in the parent widget
Imagelabel.pack(expand=True)
#
# function activated by button
def rolling_dice():
       DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
       # update image
       Imagelabel.configure(image=DiceImage)
       # keep a reference
       Imagelabel.image = DiceImage

# adding button, and command will use rolling_dice function

button = tkinter.Button(root,text='Roll the Dice',fg ='Blue',command= rolling_dice())
button.pack(expand = True)

#Calling Main loop:

root.mainloop()