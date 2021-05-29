#Python program to append,delete and display elements of list using classes

class Check:
    def __init__(self):
        self.n=[]
    def add(self,a):
        return self.n.append(a)
    def remove(self,a):
        return self.n.remove(a)
    def dis(self):
        return self.n

obj=Check()
choice=1
while(choice!=0):
    print("0.Exit")
    print("1.Add")
    print("2.Delete")
    print("3.Display")

    choice=int(input("Enter choice:"))
    if choice==1:
        n=int(input("Enter the number to append:"))
        obj.add(n)
        print("List:",obj.dis())
    elif choice==2:
        n=int(input("Enter the number to remove:"))
        obj.remove(n)
        print("List:",obj.dis())
    elif choice==3:
        print("List:",obj.dis())
    elif choice==0:
        print("Exiting")
    else:
        print("Invalid choice")
        
        
