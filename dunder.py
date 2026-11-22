class Employee:
    # __init__ is runs autoatically when we create an object of the class
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def __str__(self):
        return f"Employee ID: {self.id}, Employee Name: {self.name}"

e1= Employee(101,"John")
print(e1)  # This will call the __str__ method and print the employee details