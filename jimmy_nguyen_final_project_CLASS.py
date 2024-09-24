#-------------------------------------------------------------------------------
# Final Project
# Student Name: Jimmy Nguyen
# Submission Date: 04/28/2024
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Notes to grader: 
#-------------------------------------------------------------------------------
# Your source code below
#-------------------------------------------------------------------------------

class SmartCart(dict):
    '''dict subclass to maintain user cart'''
    def subtotal(self):
        '''Returns subtotal from a dictionary object'''
        total = 0
        #iterate over each key, value in dict
        #obtain the price and quantity for each key
        #add to total variable after multiplying price with the quantity
        for item, quantity in self.items():
            total += item.get_price() * quantity
        return total
    def tax(self):
         #your code here
         '''Computes the sales tax for the current cart contents'''
         subtotal_amount = self.subtotal()
         tax_rate = 0.043  # 4.3% tax rate for Virginia
         return subtotal_amount * tax_rate
    def total(self):
        #your code here
        '''Determines the total cost of the purchase'''
        return self.subtotal() + self.tax()
class Item(object):
    '''Item class defines an item
    available in store. Item object saved in
    lists per category'''
    
    def __init__(self, category, name, price, expiration_date):
        '''Initialization method'''
        #your code here
        #assuming all the variables are private.
        #setting all variables to self
        self.__name = name
        self.__category = category
        self.__price = price
        self.__expiration_date = expiration_date
    #define all the get methods to obtain the instance variables. 
    #define a __str__ method to obtain all four instance attributes.        
    def get_name(self):
        '''Fetches the name of the item'''
       #returing name
        return self.__name

    def get_category(self):
        '''Retrieves the category of the item'''
        #returning category
        return self.__category

    def get_price(self):
        '''Returns the price of the item'''
        #returning price
        return self.__price

    def get_expiration_date(self):
        '''Obtains the expiration date of the item'''
        #returning expiration date
        return self.__expiration_date

    def __str__(self):
        '''Provides a string representation of the item'''
        return f'{self.__name}, Category: {self.__category}, Price: {self.__price}, Expiration Date: {self.__expiration_date}'

class Dairy(Item):
    dairy_items = []
    def __init__(self, name, category, price, expiration_date, pasture_raised):
        super().__init__(name, category, price, expiration_date)
        self.__pasture_raised = pasture_raised
        Dairy.dairy_items.append(self)

    def get_spec(self):
        #your code here
        #return __pasture_raised 
        '''Retrieves the special characteristic of the item'''
        return self.__pasture_raised
#define FruitVegetable, Seafood and Poultry Subclass
#these are alll polymorphic class. 
class FruitVegetable(Item):
    veg_fruit_items = []

    def __init__(self, name, category, price, expiration_date, organic):
        #using super for category, name, price, expiration_date
        super().__init__(category, name, price, expiration_date)
        self.__organic = organic
        FruitVegetable.veg_fruit_items.append(self)

    def get_spec(self):
        return self.__organic

class Seafood(Item):
    seafood_items = []

    def __init__(self, name, category, price, expiration_date, wild_caught):
        # using super for category, name, price, expiration_date
        super().__init__(category, name, price, expiration_date)
        self.__wild_caught = wild_caught
        Seafood.seafood_items.append(self)

    def get_spec(self):
        return self.__wild_caught

class Poultry(Item):
    poultry_items = []

    def __init__(self, name, category, price, expiration_date, organic):
        # using super for category, name, price, expiration_date
        super().__init__(category, name, price, expiration_date)
        self.__organic = organic
        Poultry.poultry_items.append(self)

    def get_spec(self):
        return self.__organic

#process file
def process_file(grocery_list):
    '''Opens file, reads information, creates different category of objects'''
    dairy_items = []
    veg_fruit_items = []
    seafood_items = []
    poultry_items = []
#open file, read information, create different category of objects
    with open(grocery_list, 'r') as file:
        for line in file:
            data = line.strip().split('|')
            if len(data) == 4:
                name = data[0]
                specialty = 'No Speciality'
                category = data[1]
                price = float(data[2])
                expiration_date = data[3]
            #reading the files for 5 columns instead of the 4 with specalites
            elif len(data) ==5:
                name = data[0]
                specialty = data[1]
                category = data[2]
                price = float(data[3])
                expiration_date = data[4]

            else:
                raise ValueError('Could not match items')

            if category == 'Dairy':
                #if it is pr, it will display as pasture or non pasture
                if specialty == 'PR':
                    item = Dairy(category, name, price, expiration_date, 'Pasture')  # Swapped category and name
                else:
                    item = Dairy(category, name, price, expiration_date, 'Non Pasture')  # Swapped category and name
                dairy_items.append(item)
            elif category == 'Fruit' or category == 'Vegetable':
                #if it is or, it will display as organic or non organic
                if specialty == 'OR':
                    item = FruitVegetable(name, category, price, expiration_date, 'Organic')
                else:
                    item = FruitVegetable(name, category, price, expiration_date, 'Non Organic')
                veg_fruit_items.append(item)
            elif category == 'Seafood':
                #if it is wc, it will display as wild caught or non wild caught
                if specialty == 'WC':
                    item = Seafood(name, category, price, expiration_date, 'Wild Caught')
                else:
                    item = Seafood(name, category, price, expiration_date, 'Non Wild Caught')
                seafood_items.append(item)
            elif category == 'Poultry':
                #if it displays as or, it will display as organic or non organic
                if specialty == 'OR':
                    item = Poultry(name, category, price, expiration_date, 'Organic')
                else:
                    item = Poultry(name, category, price, expiration_date, 'Non Organic')
                poultry_items.append(item)
    #returning back all the category items
    return dairy_items, veg_fruit_items, seafood_items, poultry_items

'''
Testing code to check object creation per category list
Comment out when done. After successful completion
of class, the following code will print each item in the input file
'''



print('+++++ Dairy +++++')
for item in Dairy.dairy_items:
    print(item)

print('+++++ Fruit & Vegetable ++++')
for item in FruitVegetable.veg_fruit_items:
    print(item)

print('+++++ Seafood +++++')
for item in Seafood.seafood_items:
    print(item)

print('+++++ Poultry +++++')
for item in Poultry.poultry_items:
    print(item)






          

