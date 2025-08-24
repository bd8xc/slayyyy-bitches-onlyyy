class person:
    def __init__(self, name, occupation):
        print("Constructor called")
        self.name = name
        self.occupation = occupation

    def info(self):
        print(f"Name: {self.name}, occupation: {self.occupation}")

a = person("harry", "programmer")
b = person("rohan", "developer")
# c=person() error: missing 2 required positional arguments
print(a.name)
print(b.name)
a.info()
b.info()
