#Class variables are variables shared by all instances of a class.
#regular method - Takes the instance as the first argument
#class method - uses @classmethod (A decorator). Takes cls as first argument
#static method - static methods dont pass anything like class (cls) or instance (self)
class Employee:

    num_of_emps = 0         #Number of employees of object class
    raise_amt = 1.04        #Can be updated whenever we want 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)            #Initialising an object. Even Employee(first, last, pay) works. But cls is more general.

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:        #5 is Saturday
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)      #Uses class method

#print(emp_1.__dict__)       #prints out dictionary of values for emp_1 instance

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

#Output value of the below 3 statements is the same as a class variable has been used
print(Employee.num_of_emps)
print(emp_1.num_of_emps)
print(emp_2.num_of_emps)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

#first, last, pay = emp_str_1.split('-')

#new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016, 7, 11)

print(my_date)
print(Employee.is_workday(my_date))
