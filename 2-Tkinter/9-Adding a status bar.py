from tkinter import*   #tkinter is used to create applications with GUI

def function1():
    print('Menu item clicked!')

def function2():
    print('Saved!')

def function3():
    root.quit()

def function4():
    print("You undid")


#Main root/ main window
root = Tk()

#We create a menu
mymenu = Menu(root)

#Than we need to configure the menu
root.config(menu=mymenu)

#instead of passing root as argument, we pass mymenu to connect them directly
submenu = Menu(mymenu)

#This allows us to configure our menu, how to name our manu and to assign a submenu
mymenu.add_cascade(label ="File", menu = submenu)

#Now we go and add items to the submenu
submenu.add_command(label = "Project", command = function1)
submenu.add_command(label="Save", command = function2)

submenu.add_separator()    #create a separator line between menu items
submenu.add_command(label="Exit", command = function3)

#Create another menu
newmenu = Menu(mymenu)
mymenu.add_cascade(label="Edit",menu=newmenu)
#Add a single item to the new menu
newmenu.add_command(label="Undo",command=function4)


#We are going to create a toolbar
toolbar = Frame(root, bg="Pink")

insertbutton = Button(toolbar, text="Insert Files", command=function1)
insertbutton.pack(side=LEFT,padx=2,pady=3)

printbutton = Button(toolbar, text = "print",command=function1)
printbutton.pack(side=LEFT,padx=2,pady=3)

toolbar.pack(side=TOP,fill=X)

#WE create a status bar, bd stays for border, relief = SUNKEN gives a nice look, we place it on the west side using anchor=W
status = Label(root, text="This is the status",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM, fill=X)

#This put the window in a loop so it only closes when we hit the close button
root.mainloop()
