from abc import ABCMeta, abstractstaticmethod, abstractmethod


class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, employees):
        """ Implement in child class. """

    @abstractstaticmethod
    def print_department():
        """ Implement in child class. """


class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Accounting department: {self.employees}")


class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Development department: {self.employees}")


class ParentDeparment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees

    def print_department(self):
        print("Parent Department")
        print(f"Parent department base employees: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"Total number of employees: {self.employees}")


dept1 = Accounting(200)
dept2 = Development(400)

dept1.print_department()
dept2.print_department()

parentDept = ParentDeparment(30)

parentDept.add(dept1)
parentDept.add(dept2)

parentDept.print_department()
