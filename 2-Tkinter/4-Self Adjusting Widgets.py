from tkinter import*   #tkinter is used to create applications with GUI

#Window(Is a container) - Frame(Another Container inside Window) - Widgets


#We need to create widgets that grows in size automatically when we increase or grow the size of the window

#1-We need to create a window
root = Tk()

#We create a label
label1 = Label(root, text = "First", bg="Red", fg= "White")
label1.pack(fill=X)             #This label is adjustable to the screen width

label2 = Label(root, text = "Second", bg="Blue", fg= "Green")
label2.pack(side=LEFT, fill=Y)  #This label is adjustable to the height . side = LEFT is used to put/stick the label on the left side

#This put the window in a loop so it only closes when we hit the close button
root.mainloop()
