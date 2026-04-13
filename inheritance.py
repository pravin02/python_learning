class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name : {self.name} Age: {self.age}")


class Employee(User):

    def __init__(self, name, age, company_name, salary):
        self.name = name
        self.age = age
        self.company_name = company_name
        self.salary = salary

    def info(self):
        print(f"Name : {self.name} Age: {self.age}, company Name: {self.company_name}, Salary: {self.salary}")

emp = Employee("Pravin", "18", "UBS", 130000)
emp.info()
