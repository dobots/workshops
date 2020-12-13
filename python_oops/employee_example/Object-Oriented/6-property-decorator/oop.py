# This is like getter, setter like in other programming languages
#
# Motivation behind this is that in email, if we change either self.first of self.last then email does not change.
# If we put email as a method, then people using this class will need to change all email attributes to email methods. Big Change!
# Thus, we use getters and setters (from Java) for this 
# 

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property   #The property decorator defines a method, but we can extract it like an attribute (basically no () needed when calling it)
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter    #@<nameofproperty>.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.first) #None output!
