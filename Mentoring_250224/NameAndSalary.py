import json
from Worker import Worker, WorkerWithStatus

def extract_name_and_salary():
    with open("clients.json", "r") as file:
        data = json.load(file)
    employees = data["employees"]
    name_and_salary = [(employee["name"], employee["salary"]) for employee in employees]
    return name_and_salary

new_worker = Worker("Michal", 15, "IT", 5000)
new_worker_with_status = WorkerWithStatus("Michal", 15, "IT", 5000, "Free")

print(extract_name_and_salary())