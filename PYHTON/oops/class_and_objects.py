class person:
    name="harry"
    ocupation="programmer"
    networth=10
    def info(self):
        print(f"Name: {self.name}, Occupation: {self.ocupation}, Net Worth: {self.networth}")

a= person()
a.name="rohan"
print(a.name)
b= person()
b.name="shubham"
print(b.name)

c= person()
a.info()
b.info()
c.info()
