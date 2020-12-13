# dunder init means __init__ . THis is a special method
# More special methods in https://docs.python.org/3/reference/datamodel.html#special-method-names

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)  #usually used for logging and meant for other developers. Good to have this at least.

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)        #usually used as display for in-user

    def __add__(self, other):
        return self.pay + other.pay  #self is on left side of addition, other is on right side of addition

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.__repr__())
print(emp_1.__str__())   

#print(emp_1) #If no repr or str present, then this line just gives a vague representation of the object.
#repr(emp_1)     
#str(emp_1)   

print(int.__add__(1,2))         #inside print(1+2)
print(str.__add__('a','b'))     #inside print('a'+'b')

print(emp_1 + emp_2)

print(len(emp_1))
