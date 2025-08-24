class math:
    def __init__(self,num):
        self.num = num
    def addtonum(self, num2):
        return self.num + num2
    
    @staticmethod
    def addtwonum(num1, num2):
        """Static method to add two numbers."""
        return num1 + num2
# Example usage of the static method
m1= math(10)
result = math.addtwonum(5, 10)
print(f"The sum of 5 and 10 is: {result}")
print(m1.addtonum(5))