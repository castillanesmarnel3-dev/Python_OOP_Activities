
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working.")

    def describe(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)  
        self.team_size = team_size

    def work(self):
        super().work()
        print(f"{self.name} manages {self.team_size} people.")


manager = Manager("Ana", 80000, 5)
manager.describe()
manager.work()
