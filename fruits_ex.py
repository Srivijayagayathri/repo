# class BankAmount:
#     def __init__(self,a):
#         self.amount=a
#     def deposit(self,b):
#         self.amount+=b 
#         print("Total: ",self.amount)
#     def withdrawl(self,c):
#         self.amount -= c 
#         print("Balance: ",self.amount)

# class my_bank_det(BankAmount):
#     def __init__(self,a):
#         super().__init__(a)

    
# c=my_bank_det(10)
# c.deposit(10)


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass  # abstract method

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "dog")

    def make_sound(self):
        print("Bowbow!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "cat")

    def make_sound(self):
        print("Meow!")

# Example usage:
my_dog = Dog("Fido")
my_cat = Cat("Whiskers")
my_dog.make_sound() 
my_cat.make_sound() 

