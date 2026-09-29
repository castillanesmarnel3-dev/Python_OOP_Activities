# Parent class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working.")

    def describe(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


# Child class
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)  # reuse parent constructor
        self.team_size = team_size

    def work(self):
        # extend parent method
        super().work()
        print(f"{self.name} manages {self.team_size} people.")


# Test
manager = Manager("Ana", 80000, 5)
manager.describe()
manager.work()