from tkinter import*

root = Tk()
root.geometry("900x600")
root.title

class CreateElements:
    
    def _init_(self):
        print("This is CreateElements class")
        
    def createNewElement(self):
        label = Label(root,text ="A new label is been created using class", fg="red")
        label.pack()
        btn = Button(root, text=" Button ", command = self.message)
        btn.pack(padx=20, pady = 10)
        
    def message(self):
        messagebox.showinfo("showifo", "You clicked the button created using class")
        
obj_of_CreateElements = CreateElements = CreateElements()

btn = Button(root, text ="Click to create label and button element", command =
obj_of_CreateElements.createNewElement)
btn.pack(padx=20, pady = 10)

root.mainloop()        
"""
Created on Thu Dec  9 19:15:40 2021

@author: Admin
"""

