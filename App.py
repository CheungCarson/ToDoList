from contextlib import nullcontext
from tkinter import*

def add():
    if(input.get() != ""):
        list.delete(0,END)
        todo_list.append(input.get())
        input.delete(0,END)

        for item in todo_list:
            list.insert(END,item)

def delete():
    if(list.curselection()):
        list.delete(list.curselection())

window = Tk()
window.resizable(FALSE,FALSE)

#Listener Events for "Enter" and "Delete" keys
window.bind("<Return>", lambda event: add_btn.invoke())
window.bind("<Delete>", lambda event: complete_btn.invoke())

#Button to add task to list
add_btn = Button(window,text="Add Task",command=add)
add_btn.grid(row=0,column=0)

#Button to mark completed task
complete_btn = Button(window,text="Complete",command=delete)
complete_btn.grid(row=1,column=0,sticky=N)

#User input
input = Entry(window, font=("Arial",15))
input.grid(row=0,column=1,sticky=E)

todo_list = []

list = Listbox(window)
list.grid(row=1,column=1,sticky=E)
list.config(font=("Arial",15))

window.mainloop()