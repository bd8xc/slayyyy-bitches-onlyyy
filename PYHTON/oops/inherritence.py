class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f"Name: {self.name}, id: {self.id}")


e= employee("Alice", 101)
e.display()  # Displaying the employee details dnddnl