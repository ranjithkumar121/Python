stack=[]
size=5

def isfull():
    if len(stack)==size:
        return True
    else:
        return False
def is_empty():
    if len(stack)==0:
        return True
    else:
        return False
def push(a):
    if isfull()!=True:
        stack.append(a)
        print("pushed elements",a)
    else:
        print("stack is full")
def pop():
    if is_empty()!=True:
        return stack.pop()
    else:
        print("Stack is empty")
def sizeof():
    return len(stack)

def top_element():
    if len(stack)==0:
        return "stack is empty"
    else:
        return stack[-1]

def print_stack():
    print(stack)
    

while True:
    val=list(input().split())
    if val[0]=="push":
        push(int(val[1]))
    elif val[0]=="pop":
        print("popped element is",pop())
    elif val[0]=="size":
        print(sizeof())
    elif val[0]=="top":
        print(top_element())
    elif val[0] == "stack":
        print_stack()
    elif val[0]=="stop":
        break
    else:
        print("Give proper input")
