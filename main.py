# import tkinter
from tkinter import *
# import random module
import random

# Creating GUI window
root = Tk()
# Defining the container size, width=400, height=260
root.geometry('400x260')
# Title of the container
root.title('Love Calculator????')

# Function to calculate love percentage
# between the user and partner
def calculate_love():
    # value will contain digits between 0-9
    st = '0123456789'
    # result will be in double digits
    digit = 2
    temp = "".join(random.sample(st, digit))
    
    # Isse aapka text bhi rahega aur aage random number % ke sath dikhega
    result.config(text=f'Love Percentage between both of you: {temp}%')


# --- SAARE LABELS AUR BUTTONS FUNCTION SE BAHAR HAIN ---

# Heading on Top
heading = Label(root, text='Love Calculator - how much is he/she into you')
heading.pack(pady=5)

# Slot/input for the first name 
slot1 = Label(root, text="Enter your Name:")
slot1.pack()
name1 = Entry(root, border=5)
name1.pack(pady=2)

# Slot/input for the partner name 
slot2 = Label(root, text="Enter your partner Name:")
slot2.pack()
name2 = Entry(root, border=5)
name2.pack(pady=2)

# 'Button' ka B capital hona chahiye tha, use sahi kar diya hai
bt = Button(root, text="Calculate", height=1, width=9, command=calculate_love)
bt.pack(pady=10)

# Text on result slot
result = Label(root, text='Love Percentage between both of you: -- %')
result.pack(pady=5)

# Starting the GUI
root.mainloop()
