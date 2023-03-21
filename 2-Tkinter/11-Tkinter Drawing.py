from tkinter import*


root = Tk()

#Create a Canva , Specify width and height
canvas = Canvas(root,width=200,height=100)
#Pack the canva to the main root
canvas.pack()

#Create a line, Specify the coordinates
newline = canvas.create_line(0,0,50,100)

#Create another line , Fill = "green" is used for color1
otherline= canvas.create_line(10,10,100,100, fill="green")

#This put the window in a loop so it only closes when we hit the close button
root.mainloop()
