class person:
    def __init__(self,name,age):
        self.__name = name
        self.age = age

    #getter for name
    def get_name(self):
        return self.__name
    #setter for name
    def set_name(self,name):
        self.name= name
    #getter for age
    def get_age(self):
        return self.age
    #setter for age
    def set_age(self, age):
        self.age = age

# Example usage
p = person("alice", 30)  # Creating an instance of the person class
p.set_name("Doe")  # Setting a new name using the setter
print(p.get_name())  # Accessing the name using the getter

print(p.get_name())  # Accessing the updated name using the getter
print(p.get_age())  # Accessing the age using the getter
p.set_age(35)  # Setting a new age using the setter
print(p.get_age())  # Accessing the updated age using the getter