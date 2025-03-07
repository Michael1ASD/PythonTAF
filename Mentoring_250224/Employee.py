# Klasa employees
# ZROBIONE
# Konstruktor przyjmuje nazwę pliku
# ZROBIONE
# Obiekt Employees zawiera listę obiektów Worker
# ZROBIONE
# Funkcja która zwraca listę pracowników którzy mają zadany status (w klasie employees)
# ZROBIONE

import json

class Worker:
    def __init__(self, name, age, department, salary, status=None, street=None, city=None, state=None, zip_code=None,
                 project_name=None, project_start_date=None, project_end_date=None):
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary
        self.status = status
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.project_name = project_name
        self.project_start_date = project_start_date
        self.project_end_date = project_end_date

    def __repr__(self):
        return (f"Worker(name={self.name}, age={self.age}, department={self.department}, "
                f"salary={self.salary}, status={self.status}, "
                f"address=(street={self.street}, city={self.city}, state={self.state}, "
                f"zip_code={self.zip_code}), project=(name={self.project_name}, "
                f"start_date={self.project_start_date}, end_date={self.project_end_date}))")

class Employee:
    def __init__(self, imported_file):
        self.workers = self.get_all_workers(imported_file)

    def get_all_workers(self, imported_file):
        with open(imported_file, "r") as file:
            data = json.load(file)
            all_workers = []
            for worker_data in data["employees"]:
                worker = Worker(
                    name=worker_data.get("name"),
                    age=worker_data.get("age"),
                    department=worker_data.get("department"),
                    salary=worker_data.get("salary"),
                    status=worker_data.get("status"),
                    street=worker_data.get("address", {}).get("street"),
                    city=worker_data.get("address", {}).get("city"),
                    state=worker_data.get("address", {}).get("state"),
                    zip_code=worker_data.get("address", {}).get("zip"),
                    project_name=worker_data.get("project", {}).get("name"),
                    project_start_date=worker_data.get("project", {}).get("start_date"),
                    project_end_date=worker_data.get("project", {}).get("end_date"),
                )
                all_workers.append(worker)
            return all_workers

    def get_workers_with_status(self, status):
        return [repr(worker) for worker in self.workers if worker.status == status]


employee_manager = Employee('clients.json')
print(employee_manager.get_workers_with_status("True"))
