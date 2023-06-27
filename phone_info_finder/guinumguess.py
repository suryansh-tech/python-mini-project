# for GUI 
from tkinter import *
from PIL import ImageTk,Image

import random
import tkinter.messagebox as tmsg

# function that generates random number
def generate():
    global comp #make it global for outside use
    comp = random.randint(1, 50)

# this funtion will have all configuration of ui
# screen - title, geo of screen, min and max etc

#initization the app window
app = Tk()

def basic():
    # setup the window size, title, logo
    app.title("Number Guessing game")
    app.geometry("450x500")
    app.minsize(450, 500)
    app.maxsize(450, 500)
    # adding pic and icon
    photo = PhotoImage(file="guess.png")
    app.iconphoto(False, photo)
    #heading
    heading = Label(app, text='Number Guessing game', font="Helvicta 18 bold", bg='black', fg='tomato', padx=170, pady=10).pack()
    
    #text read file
    with open('score.txt', 'r')as f:
        hg = f.read() #txt file ka sab hg m store ho jana h

    # score
    sc = Label(app, text=f'Last High score: {hg}', font="lucida 10 bold").pack(padx=25, pady=10)

    # footer
    footer = Label(app, text='Developed by Suryansh porwal', font="Helvicta 15 bold", bg='black', fg='tomato', padx=153, pady=15).pack(side=BOTTOM) #side= bootom m kr dega

# Declaring result function which will validate the user input and display message according to user input.
def result():
    global count
    num = uservar.get()
    if num == '':
        tmsg.showerror('Error',"Please enter a value")
    else:
        n = int(num)
        count += 1
        if count == 10:
            a = tmsg.showinfo('Game over',"You loose the Game!")
        elif comp == n:
            score = 11 - count #score stores a int value
            a = tmsg.showinfo('Winnnnnnnnnnnnnn!',' wooo you won ') 
            # storing the win score in txt file
            with open('score.txt', 'w') as f:
                f.write(str(score)) #as score store a inter valye so we have to convert it str
                generate()
                tmsg.showinfo('Next Number',f'click ok to guess amother number')
        elif comp>n:
            show.config(text='Select greater number',fg='red')
        else:
            show.config(text='Select smaller number',fg='red')        

#This function shows a dialog box to the user of a particular message. Then restart it again.
def restart():
    tmsg.showerror("Reset","Game reset")
    generate()  

basic()
    
# count
count = 0
comp = random.randint(1, 50) # generating random values between 1 to 50

#input fiels or we can say a entry for number
uservar = StringVar() # a variable to getting input in string
user = Entry(app, textvariable=uservar, font='Helvicta 18 bold', borderwidth=2, relief=FLAT, justify=CENTER).pack()

# adding a image
i = Image.open('guess.png', mode='r')
img = ImageTk.PhotoImage(i)
l = Label(image=img).pack(pady=15)

# subbmit button
i = Image.open('bt.png')
resized_image = i.resize((150, 50))
new_image = ImageTk.PhotoImage(resized_image)
submit = Button(app, image=new_image, command=result, font='Helvicta 18 bold', relief=FLAT).pack() #The Button Function is used to submit the guessed value by the user.

# showing text
show = Label(app, text='', font='Helvicta 12 bold')
show.pack(pady=7)

# looping our app
app.mainloop()    