#1-We need to import tkinter
from tkinter import *
#2-We import parser, is going to help us with mathematical equations



#7-Get the user input and display it in the textfield, and add this function as a command action to every number button
i = 0
def get_variables(num):
    global i
    display.insert(i,num) #i is used as an index, so we insert first num at index 0, than we increment the global variable i for other inserts
    i+=1

#8-Clear all function
def clear_all():
    display.delete(0,END)   #we need to specify the first position and the end positon


#9-Delete a single element from the textfield
def undo():
    entire_string = display.get()  #extract the entire string from the display
    if len(entire_string)>0:
        new_string = entire_string[:-1]    #save the entire_string without the last element in new_string if length of entire_string > 0 (if we have typed smthng in the textfield)
        clear_all()                        #clear the entire string
        display.insert(0,new_string)       #display the new string. Insert the new string from position 0
    else:
        clear_all()                        #Else, if there is nothing on the screen clear the screen, and display error
        display.insert(0,"Error")


#10-Function to display operators in the input field
def display_operation(operator):
    global i                            #we use the global i to keep the index so whenever we add something in input field it will be added according to the index
    length = len(operator)              #we save the length of operator in order to increment the index in propper form
    display.insert(i,operator)          #we display the operator from current state of index
    i+=length                           #increment the global i with operator length


#11-Calculate
def calculate():
    entire_string = display.get()                   #we store the entire string in this variable
    try:
        #a = parse.expr(entire_string).compile()     #we pass the entire string to the parser
        result = eval(entire_string)                 #save the result , and make the calculations using eval()
        clear_all()                                  #clear the screen
        display.insert(0,result)                     #display the result
    except Exception:
        clear_all()
        display.insert(0,"Error")


#3-Create the root window
root = Tk()
root.title('Calculator')  #We set a title


#4-Adding the input field, when we press a number it is going to apper here in this field
display = Entry(root)
#If we use .grid(row = '',column=''), we can display the button without using .pack()
display.grid(row=1,columnspan=6,sticky=W+E)


#5-Adding buttons to the calculator
Button(root,text='1', command = lambda :get_variables(1) ).grid(row=2,column=0) #we used lambda to handle the button click. Same as: command=get_variables(1)
Button(root,text='2',command = lambda :get_variables(2) ).grid(row=2,column=1)
Button(root,text='3',command = lambda :get_variables(3) ).grid(row=2,column=2)

Button(root,text='4',command = lambda :get_variables(4) ).grid(row=3,column=0)
Button(root,text='5',command = lambda :get_variables(5) ).grid(row=3,column=1)
Button(root,text='6',command = lambda :get_variables(6) ).grid(row=3,column=2)

Button(root,text='7',command = lambda :get_variables(7) ).grid(row=4,column=0)
Button(root,text='8',command = lambda :get_variables(8) ).grid(row=4,column=1)
Button(root,text='9',command = lambda :get_variables(9) ).grid(row=4,column=2)

#6-Adding other buttons to calculator: +,-,*,/,clear
Button(root,text='AC', command= lambda :clear_all() ).grid(row=5,column=0)
Button(root,text='0',command = lambda :get_variables(0)).grid(row=5,column=1)
Button(root,text='=', command= lambda: calculate()).grid(row=5,column=2)

Button(root,text='+', command = lambda: display_operation('+') ).grid(row=2,column=3)
Button(root,text='-', command = lambda: display_operation('-') ).grid(row=3,column=3)
Button(root,text='*', command = lambda: display_operation('*') ).grid(row=4,column=3)
Button(root,text='/', command = lambda: display_operation('/') ).grid(row=5,column=3)

#Adding new operations
Button(root,text='pi', command = lambda: display_operation('*3.14') ).grid(row=2,column=4)
Button(root,text='%', command = lambda: display_operation('%') ).grid(row=3,column=4)
Button(root,text='(', command = lambda: display_operation('(') ).grid(row=4,column=4)
Button(root,text='exp', command = lambda: display_operation('**') ).grid(row=5,column=4)

Button(root,text='<-', command=lambda :undo() ).grid(row=2,column=5)   #backspace
Button(root,text='x!', command = lambda: display_operation('x!') ).grid(row=3,column=5)   #factorial
Button(root,text=')', command = lambda: display_operation(')') ).grid(row=4,column=5)
Button(root,text='^2', command = lambda: display_operation('**(1 / 2)') ).grid(row=5,column=5)   #square root of a number



#This put the window in a loop so it only closes when we hit the close button
root.mainloop()
