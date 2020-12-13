#2nd Oct 2020
#All these are instance variables present here. 
class Employee:
	#self refers to the instance
    def __init__(self, first, last, pay):
        self.first = first			#Can also be self.fname = first. But usually the same variable name is used. 
        self.last = last			#For emp_1 its equivalent to emp_1.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    #method within class to print full name
    #self is the instance of the class
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)	#instance names are passed on automatically to the self keyword 
emp_2 = Employee('Test', 'Employee', 60000)


print(emp_1.email)
print(emp_1.fullname())						#returns the method for a class. Therefore () is important, gives error without it as the instance is given automatically when the method is called.
print(Employee.fullname(emp_1))				#In the background the previous line gets transformed to this.