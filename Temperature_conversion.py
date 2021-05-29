temp=input("Enter the temperature to covert? (e.g., 45F,102c etc) : ")
degree=int(temp[:-1])
con=temp[-1]
if con.upper()=="C":
    result=int((9*degree)/5+32)
    con="Fahrenheit"
elif con.upper()=="F":
    result=int((degree-32)*5/9)
    com="Celsius"
else:
    print("Input proper conversion")
    quit()
print("The temperature in",con,"is",result)