class Worker:
    def __init__(self, name, age, department, salary):
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

class WorkerWithStatus(Worker):
    def __init__(self, name, age, department, salary, status):
        super().__init__(name, age, department, salary)
        self.status = status

class WorkerWithAllAttributes:
    def __init__(self, name, age, department, salary, contact, status, address):
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary
        self.contact = contact
        self.status = status
        self.address = address

