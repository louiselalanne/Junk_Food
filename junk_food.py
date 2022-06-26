from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.geometry("900x500")

style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "white", background= "orange", foreground='orange')
root.option_add("*TCombobox*Listbox*Background", 'white')
root.option_add('*TCombobox*Listbox*Foreground', 'orange')

burger = ImageTk.PhotoImage(Image.open("comidas.png"))
burger_img = Label(root)
burger_img["image"] = burger
burger_img.place(relx=0.7, rely=0.5, anchor=CENTER)

title = Label(root, text="Louis Junk Food 😄", font=("times", 30, "bold"), fg="saddle brown")
title.place(relx=0.2, rely=0.1, anchor=CENTER)

label = Label(root, text="Select Dish", font=("times",15), fg="orange")
label.place(relx=0.06, rely=0.2, anchor=CENTER)

#---------dropdown-LACNHES
dish=["burger", "fries"]
lanches_dropdown = ttk.Combobox(root, state="readonly", value = dish)
lanches_dropdown.place(relx=0.25, rely=0.2, anchor=CENTER)

label_addons = Label(root, text="Select Add-Ons", font=("times",15), fg="orange")
label_addons.place(relx=0.08, rely=0.5, anchor=CENTER)

#---------dropdown-ADDONS
toppings=[]
toppings_dropdown = ttk.Combobox(root, state="readonly", values = toppings)
toppings_dropdown.place(relx=0.25, rely=0.5, anchor=CENTER)

#---------Amount
dish_amount = Label(root, font=("times",15, "bold"), fg="orange")
dish_amount.place(relx=0.2, rely=0.75, anchor=CENTER)

class parent():
    def __init__(self):
     print("this is parent class")
     
    def menu(dish):
        if dish=="burger":
            print("You can add following toppings")
            toppings=["cheese","bacon"]
            toppings_dropdown["values"]=toppings
            print("More cheese | Add bacon")
        elif dish=="fries":
            toppings=["cheese","bacon"]
            toppings_dropdown["values"]=toppings
            print("Add cheese | Add bason")
        else:   
            print("please enter valid dish")
            
    def final_amount(dish, add_ons):
        if dish=="burger" and add_ons=="cheese":
            dish_amount["text"]="You need to pay 1 USD"
            print("You need to pay 250 USD")
        elif dish=="burger" and add_ons=="bacon":
            dish_amount["text"]="You need to pay 2 USD"
            print("You need to pay 350 USD")
        elif dish=="fries" and add_ons=="cheese":
            dish_amount["text"]="You need to pay 3 USD"
            print("You need to pay 250 USD")
        elif dish=="fries" and add_ons=="bacon":
            dish_amount["text"]="You need to pay 4 USD"
            print("You need to pay 450 USD")
            
            
class child1(parent):
    def __init__(self,dish):
        self.new_dish = dish
        
    def  get_menu(self):
        new_dish=lanches_dropdown.get()
        parent.menu(new_dish)
        
class child2(parent):
    def __init__(self,dish,addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_final_amount(self):
        new_dish=lanches_dropdown.get()
        addons=toppings_dropdown.get()
        parent.final_amount(new_dish,addons)

child1obj = child1(lanches_dropdown.get())
child1obj.get_menu()

child2obj = child2(toppings_dropdown.get(), lanches_dropdown.get())
child2obj.get_final_amount()

btn_add = Button(root, text="Check Add-Ons", command=child1obj.get_menu, bg="DarkOrange", fg="white", relief= FLAT)
btn_add.place(relx=0.06, rely=0.3, anchor=CENTER)

btn_amount = Button(root, text="Amount", command=child2obj.get_final_amount, bg="DarkOrange", fg="white", relief= FLAT)
btn_amount.place(relx=0.04, rely=0.6, anchor=CENTER)

root.mainloop()