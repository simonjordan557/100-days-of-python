import tkinter

FONT = ("arial", 18, 'bold')

def calculate():
    output_label.config(text=round(int(miles_entry.get()) * 1.609))

window = tkinter.Tk()
window.title("Miles to KM Converter")
window.minsize(width=400, height=300)
window.config(padx=25, pady=25)

miles_entry = tkinter.Entry(width=6, font=FONT)
miles_entry.config()
miles_entry.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles", font=FONT)
miles_label.config(padx=10, pady=10)
miles_label.grid(row=0, column=2)

is_equal_to_label = tkinter.Label(text="is equal to", padx=10, pady=10, font=FONT)
is_equal_to_label.grid(row=1, column=0)

output_label = tkinter.Label(text="", padx=10, pady=10, font=FONT)
output_label.grid(row=1, column=1)

km_label = tkinter.Label(text="km", padx=10, pady=10, font=FONT)
km_label.grid(row=1, column=2)

button = tkinter.Button(text="Calculate", command=calculate, font=FONT)
button.grid(row=2, column=1)





# window.title("First GUI Program")
# window.minsize(width=640, height=480)
#
# my_label = tkinter.Label(text="Label 1", font=("courier", 24, "bold"))
# my_label.grid(row=0, column=0)
#
# my_label.config(text="Altered Text")
#
# my_button = tkinter.Button(text="Click Me!", command=clicked)
# my_button.grid(row=1, column=1)
#
# my_new_button = tkinter.Button(text="No, click me!", command=clicked)
# my_new_button.grid(row=0, column=2)
#
# my_entry = tkinter.Entry(width=10)
# my_entry.grid(row=2, column=3)


# from tkinter import *
#
# #Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
#
# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
#
# #Buttons
# def action():
#     print("Do something")
#
# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()
#
# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()
#
# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()
#
#
#
#
# def add(*args):
#     ret = 0
#     for n in args:
#         ret += n
#     return ret
#
# print(add(1, 3, 5, 7))
# print(add(2, 4))






window.mainloop()

