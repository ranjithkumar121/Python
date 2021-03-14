#01:23:34
def addTime(t1,t2):
    s = int(t1[6:8]) + int(t2[6:8])
    m = int(t1[3:5]) + int(t2[3:5])
    h = int(t1[0:2]) + int(t2[0:2])
    if s > 59:
        secs = s - 60
        m1 = m + 1
    else:
        secs = s
        m1 = m
    if m1 > 59:
        mins = m1 - 60
        h1 = h + 1
    else:
        mins = m1
        h1 = h
    if h1 > 23:
        hrs = h1 - 24
    else:
        hrs = h1

    print(hrs,":",mins,":",secs)

t1=str(input('Time1:'))
t2=str(input('Time2:'))
addTime(t1,t2)




