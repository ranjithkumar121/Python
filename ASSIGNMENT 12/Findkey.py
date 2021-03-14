def findkey(input1,input2,input3):
    ss=""
    if len(input1)==4 and len(input2)==4 and len(input3)==4:
        max1=min(int(input1[0]),int(input2[0]),int(input3[0]))
        max2=min(int(input1[1]),int(input2[1]),int(input3[1]))
        max3=min(int(input1[2]),int(input2[2]),int(input3[2]))
        max4=min(int(input1[3]),int(input2[3]),int(input3[3]))
    ss=str(max1)+str(max2)+str(max3)+str(max4)
    return int(ss)

input1='3521'
input2='2452'
input3='1352'
ss=findkey(input1,input2,input3)
print(type(ss))
print(ss)