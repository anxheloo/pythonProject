from tkinter import*   #tkinter is used to create applications with GUI


class MyButtons:

    def __init__(self,rootone):
        frame = Frame(rootone)
        frame.pack()

        self.printbutton = Button(frame, text = "Click Here", command=self.printmessage)
        self.printbutton.pack()

        self.quitbutton = Button(frame, text = "Exit", command=frame.quit)  #frame.quit -> .quit is an inbuild method
        self.quitbutton.pack(side = LEFT)

    #Outside of the init method
    def printmessage(self):
        print("Button Clicked")



#Main root/ main window
root = Tk()

#Once we created the MyButtons object and starts the app, root is initialized, b is initialized with all the lines inside it
b = MyButtons(root)


#This put the window in a loop so it only closes when we hit the close button
root.mainloop()
