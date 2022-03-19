from tkinter import Tk, Button, Label, DoubleVar, Entry, ttk                                #importing libraries



window = Tk()                                                                               #creating an application and storing it
window.title("Feet To Meter Conversion App")                                                #giving the name to application
window.configure(background = "gray70")                                                     #giving background color to the application
window.geometry("400x250")                                                                  #setting dimensions of application
window.resizable(width = False, height = False)                                             #adjustment of window (resizable or nonresizable)

def convert():                                                                              #defining convert function
    value = float(ft_entry.get())
    meter = value * 0.3048
    mt_value.set("%.4f" % meter)

def clear():                                                                                #definin clear function
    ft_value.set("")
    mt_value.set("")


### FEET ###
ft_label = Label(window, text = "Feet",  bg = "light blue", fg = "black", width = 25, height = 3)       #specifiying some parameters and labeling it
ft_label.grid(column = 0, row = 0, padx = 15, pady = 15)                                                #gridding it in application window

ft_value = DoubleVar()                                                                                  #inserting the data type that expecting
ft_entry = Entry(window, textvariable = ft_value, width = 12, font=('Georgia 16'))                      #creating the entry widget and defining some parameters
ft_entry.grid(column = 1, row = 0, ipadx = 10, ipady = 15)                                              #gridding it in application window
ft_entry.delete(0, "end")                                                                               #clearing the widget when the program starts



### METER ###
mt_label = Label(window, text = "Meter", bg = "light blue", fg = "black", width = 25, height = 3)       #specifiying some parameters and labeling it
mt_label.grid(column = 0, row = 1, padx = 15, pady = 15)                                                #gridding it in application window

mt_value = DoubleVar()                                                                                  #inserting the data type that expecting
mt_entry = Entry(window, textvariable = mt_value, width = 12, font=('Georgia 16'))                      #creating the entry widget and defining some parameters
mt_entry.grid(column = 1,  row = 1, ipadx = 10, ipady = 15)                                             #gridding it in application window
mt_entry.delete(0, "end")                                                                               #clearing the widget when the program starts


### CONVERT ###
convert_button = Button(window, text = "Convert", bg = "pale green", fg = "black", height = 3, width = 20, command = convert)   #creating Convert button and defining its parameters
convert_button.grid(column = 0, row = 3, padx = 15, pady = 15)                                                                  #gridding the button

### CLEAR ###
clear_button = Button(window, text = "Clear", bg = "light coral", fg = "black", height = 3, width = 20,  command = clear)       #creating Clear button and defining its parameters
clear_button.grid(column = 1, row = 3, padx = 15, pady = 15)                                                                    #gridding the button



window.mainloop()                                                               #it will loop forever until the user exits the window or waits for any events from the user
