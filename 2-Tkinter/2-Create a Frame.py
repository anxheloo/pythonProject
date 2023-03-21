from tkinter import*   #tkinter is used to create applications with GUI

#Window(Is a container) - Frame(Another Container inside Window) - Widgets

#1-We need to create a window
root = Tk()

#2-We create the frame
newframe = Frame(root)
newframe.pack()        #add frame to the window

otherframe = Frame(root)
otherframe.pack(side=BOTTOM)      #add frame to the window. side=BOTTOM takes this frame and put in bottom

#3-Lets create some widgets
button1 = Button(newframe,text="Click Here",fg="Red")  #We created a button, set it on the firstframe, gave it a text & a foreground color
button2 = Button(otherframe,text="Click Here",fg="Blue")

button1.pack()    #add the button to our layout(window)
button2.pack()    #add the button to our layout(window)

#This put the window in a loop so it only closes when we hit the close button
root.mainloop()
