time=int(input("Enter time in hours:"))
if time < 12 or time==24:
    print("Good morning")
elif time >= 12 and time < 18:
    print("Good evening")
elif time >=18 and time <24:
    print("Good night")