#class Developer and Manager inherit the Employee class
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


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)      #firstname,lastname and pay are handled in the Employee class
        #Employee.__init__(self, first, last, pay) #This line also works, but for maintainability the above is preferred.
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):       #Never pass mutable obects like lists and dictionaries as default values. That's why None.
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(dev_1.last)
print(dev_1.prog_lang)

print(mgr_1.email)
#print(help(Developer)) #prints the visualisation about the object

mgr_1.add_emp(dev_2)
mgr_1.print_emps()
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()

print(isinstance(mgr_1, Manager))       #Checks if mgr_1 is an instance of Manager
print(issubclass(Developer, Employee))