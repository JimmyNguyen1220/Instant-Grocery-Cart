#import class from class file
from jimmy_nguyen_final_project_CLASS import SmartCart, Dairy, FruitVegetable, Seafood, Poultry, process_file
#import GUI Module
from tkinter import Tk, Frame, Label, Button, Checkbutton, IntVar, StringVar, Entry, TOP
from functools import partial
import random, string #used in random receipt no function


class MyFrame(Frame):
    def __init__(self, root):
        '''Constructor method'''
        Frame.__init__(self, root) #Frame class initialization
        self.init_container() #initialize all widget containers
        self.cart = SmartCart() #initialize SmartCart dict object - key = Item object item selected, value = quantity
        self.welcome() #start the application
        self.data = StringVar(self, 'Subtotal: 0.0') #Associated with subtotal label


        
    def init_container(self):
        '''Initialize widget containers'''
        self.quantity_entries = [] #qunatity entry list
        self.states = [] #holds state if selected/not i-th list item holds selection for i-th item
 
    def clear_frame(self): 
        '''Clears the previous frame'''
        for widget in self.winfo_children():
            widget.destroy()

    def exit_application(self):
        '''Exits the program'''
        root.destroy()

 
    def welcome(self):
        '''1. Welcome window - refer spec file for details'''
        self.clear_frame()
        Label(self, text = '****Welcome to Instant Cart!****', background="gray70").pack(side = TOP)
        #your code here
        #Start Ordering: Button – start the program, command
        #creating the start ordering button, for users to enter the application
        Button(self, text='start ordering', command=self.shop_by_category).pack(side=TOP)
        #Exit Application: Button – exit the program, command = exit_application
        #creating the exit application button for users to exit the program
        Button(self, text='exit application', command=self.exit_application).pack(side=TOP)
        

    def shop_by_category(self):
        '''2. Widget to display different category of items - refer spec file for details'''
        self.clear_frame()
        self.init_container()
        #your code here
        #a.	Choose Category: label
        Label(self, text='choose category').pack()
        #b.	Dairy: Button – command = start (code below)
        #partial is a special method to pass an argument during button command
        #for dairy category Item.dairy_items will be passed to display all dairy item
        self.dairy_button  = Button(self, text = 'dairy', command=partial(self.start, Dairy.dairy_items))
        self.dairy_button.pack()
        #your code here
        #c.	Vegetable and Fruit - veg_fruit_button: Button – command = start (Same as dairy)
        #using args for the fruitvegetable button and the items
        veg_fruit_button = Button(self, text='vegetable and fruit', command=partial(self.start, FruitVegetable.veg_fruit_items))
        veg_fruit_button.pack()
        #d.	Poultry and Meat - poultry_meat_button: Button – command = start(Same as dairy)
        # using args for the poultry button and the items
        poultry_meat_button = Button(self, text='poultry and meat', command=partial(self.start, Poultry.poultry_items))
        poultry_meat_button.pack()
        #e.	Seafood: Button - seafood_button – command = start(Same as dairy)
        # using args for the seafood button and the items
        seafood_button = Button(self, text='seafood', command=partial(self.start, Seafood.seafood_items))
        seafood_button.pack()
        #f.	Go Back: Button – command = welcome (go back to #1)
        go_back_button = Button(self, text='go back', command=self.welcome)
        go_back_button.pack()
        #layout manager for all the widgets
        for widget in self.winfo_children():
            widget.pack(pady=5)

    def start(self, current_items):
        ''''3. Start ordering from selected category,
        list passed by command will be used as current_items'''
        self.clear_frame()
        self.init_container()
        print(current_items)
        #creating widgets for items using a for loop
        #iterative over each item of current items and
        #create that many checkbutton, price, exp date and specialty label,and quantity entry
        row = 0#########
        for item in current_items:
            self.states.append(IntVar()) #keeps track if an item is selected
            checkbutton = Checkbutton(self, text=item.get_name(), variable=self.states[row])#create check buttons
            checkbutton.grid(row = row, column = 0)

            #your code here
            #create and layout a price label, set text to item.get_price()
            price_label = Label(self, text='price: $' + str(item.get_price()))
            price_label.grid(row=row, column=1, padx=12, pady=5, sticky='w')
            #create and layout a quantity entry and append to quantity_entries, set width = 2
            quantity_entry = Entry(self, width=5)
            quantity_entry.grid(row=row, column=2, padx=12, pady=5, sticky='w')
            self.quantity_entries.append(quantity_entry)
            #create and layout exp_date_label and set text to item.get_expiration_date() method
            exp_date_label = Label(self, text='exp. Date: ' + item.get_expiration_date())
            exp_date_label.grid(row=row, column=3, padx=12, pady=5, sticky='w')
            #create and layout speciality_label and set text to item.get_spec() method
            specialty_label = Label(self, text='specialty: ' + item.get_spec())
            specialty_label.grid(row=row, column=4, padx=12, pady=5, sticky='w')
            #adding each row onto the other
            row += 1
        
        #create and layout subtotal label, set textvaribale = self.data so it changes
        #with each add_to_cart button being pressedng
        subtotal_label = Label(self, textvariable=self.data)
        subtotal_label.grid(row=row, columnspan=5, padx=12, pady=5, sticky='w')
        #create and layout select categories: button, command = shop_by_category
        select_categories_button = Button(self, text='select categories', command=self.shop_by_category)
        select_categories_button.grid(row=row + 1, column=0, padx=12, pady=5, sticky='w')
        #create and layout add_to_cart_button, command = partial(self.add_to_cart, current_items)
        #using args for current items
        add_to_cart_button = Button(self, text='add to cart', command=partial(self.add_to_cart, current_items))
        add_to_cart_button.grid(row=row + 1, column=1, padx=12, pady=5, sticky='w')
        #create and layout button: checkout, command = self.checkout
        checkout_button = Button(self, text='checkout', command=self.checkout)
        checkout_button.grid(row=row + 1, column=2, padx=12, pady=5, sticky='w')

    def add_to_cart(self, current_items): #####
        '''3. Added to cart, displays subtotal - see spec file for details layout'''
        for i in range(len(current_items)):
            #your code here
            #get() the value of i-th item of self.states -> returns 1 if selected otherwise 0
            #if item is selected:
                #get the product quantity from quantity_entries using get() function
                #add item to self.cart dict where k = item object, v = quantity
            if self.states[i].get() == 1:  # Check if the item is selected
                quantity = int(self.quantity_entries[i].get())  # Get the quantity entered by the user
                item = current_items[i]  # Get the current item
                self.cart[item] = quantity  # Add the item and its quantity to the cart
        #your code here
        #set the StringVar to be the current subtotal (SmartCart object self.cart has subtotal method)
        #refer to class file
        subtotal_amount = self.cart.subtotal()
        #setting the data to the proper formatting of subtotal
        self.data.set('Subtotal: ${:.2f}'.format(subtotal_amount))
    def get_receipt_number(self):
        '''Generate random receipt number'''
        #creating a random receipt number for the application
        return  ''.join(random.choices(string.ascii_letters.upper() + string.digits, k=4))

    def checkout(self):
        '''4. Check out window '''
        self.clear_frame()
        #your code here to create and layout following widgets:
        #refer to receipt frame
        #    Your e-receipt: Label
        #    Receipt Number: Label - Randomly generated by program - text = get_receipt_number()
        Label(self, text='Your e-receipt').pack()
        Label(self, text='Receipt Number: ' + self.get_receipt_number()).pack()
        #	Name Price Quantity Expiration Date, Speciality: Header Label
        #	Item purchased, price quantity, exp.date, specialty: Label - from cart dictionary using self.cart.items()
        Label(self, text='Name Price Quantity Expiration Date, Speciality').pack()
        for item, quantity in self.cart.items():
            Label(self,
                  text=f'{item.get_name()} {item.get_price()} {quantity} {item.get_expiration_date()} {item.get_spec()}').pack()
        #	Subtotal: Label - get self.cart subtotal - new label
        #	Tax: Label - 4.3%
        #	Total: Label - subtotal + tax
        Label(self, text=f'Subtotal: {self.cart.subtotal()}').pack()
        Label(self, text='Tax: 4.3%').pack()
        Label(self, text=f'Total: {self.cart.total()}').pack()
        #	‘Thank you’ message: Label
        #	Exit application: Button – exit the program- command = exit_application
        Label(self, text='Thank you').pack()
        Button(self, text='Exit application', command=self.exit_application).pack()
        

#main driver code
#your code here
process_file('grocery_list.txt')
#create root window
root = Tk()
root.title('Instant Cart') #set window title
#your code here
#create a myframe object and layout
app = MyFrame(root)
app.pack()
#call mainloop
root.mainloop()
