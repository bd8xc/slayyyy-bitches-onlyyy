class myclass:
    def __init__(self, name):
        self.__name = name  # private variable

    @property
    def name(self):
        """Getter for the name property."""
        return self.__name
    
object = myclass("John")
print(object.name)  # Accessing the name property using the getter