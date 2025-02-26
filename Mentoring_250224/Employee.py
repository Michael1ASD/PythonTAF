# +Klasa employees
# ZROBIONE

# +Konstruktor przyjmuje nazwę pliku
# ZROBIONE

# Obiekt Employees zawiera listę obiektów Worker
# BRAK

# Funkcja która zwraca listę pracowników którzy mają zadany status (w klasie employees)
# ZROBIONE

import json
# from Worker import WorkerWithAllAttributes

class Employees:
    def __init__(self, imported_file):
        self.imported_file = imported_file
        self.employees = self.return_all_employees()

    def return_all_employees(self):
        with open(self.imported_file, "r") as file:
            data = json.load(file)
            return data["employees"]

    def return_employees_with_true_status(self, status):
        employees_with_true_status = [employee for employee in self.employees if employee.get("status") == status]
        return employees_with_true_status

new_employee = Employees("clients.json")
print(new_employee.return_employees_with_true_status("True"))