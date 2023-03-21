from tkinter import*
import tkinter.messagebox   #we have to import this for message box

root = Tk()
tkinter.messagebox.showinfo("Title","This is awesome")

#Message box that ask a question and accept the response. We save the response in a variable and based on it, we execute another code
response = tkinter.messagebox.askquestion("Question 1","Do you like coffee")
if response == "yes":
    print("Here is a coffee for you!")


#This put the window in a loop so it only closes when we hit the close button
root.mainloop()
