#Python program to find area of rectangle using classes

class  rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth

l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
a=rectangle(l,b)
result=a.area()
print("The area is",result)
