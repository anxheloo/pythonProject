from tkinter import*   #tkinter is used to create applications with GUI

#We will create a program that when we hit a button, some text will be displayed on the screen

#We need to create a window
root = Tk()

#We create a function with the action we want to happen after we click
def dosomething():
    print("You clicked the button")

#Now we create the button and add : command = dosomething, when we click the button, terminal will print.
button1 = Button(root, text = "Click Here", command=dosomething)   #if we use command = dosomething(), this will execute the method once,
                                                                   #thats why we use command = dosomething without '()'

#If we use  button1 = Button(root, text = "Click Here", command=dosomething).grid(row = '',column=''), we can display the button without using .pack()
button1.pack()

#This put the window in a loop so it only closes when we hit the close button
root.mainloop()
