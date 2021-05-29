Prime Game (100 Marks)
Rax, a school student, was bored at home in the pandemic. He wanted to play but there was no one to play with. He was doing some mathematics questions including prime numbers and thought of creating a game using the same. After a few days of work, he was ready with his game. He wants to play the game with you.


GAME:

Rax will randomly provide you a range [ L , R ] (both inclusive) and you have to tell him the maximum difference between the prime numbers in the given range. There are three answers possible for the given range.

There are two distinct prime numbers in the given range so the maximum difference can be found.

There is only one distinct prime number in the given range. The maximum difference in this case would be 0.

There are no prime numbers in the given range. The output for this case would be -1.


To win the game, the participant should answer the prime difference correctly for the given range.


Example:

Range: [ 1, 10 ]

The maximum difference between the prime numbers in the given range is 5.

Difference = 7 - 2 = 5


Range: [ 5, 5 ]

There is only one distinct prime number so the maximum difference would be 0.


Range: [ 8 , 10 ]

There is no prime number in the given range so the output for the given range would be -1.


Can you win the game?



Input Format
The first line of input consists of the number of test cases, T

Next T lines each consists of two space-separated integers, L and R



Constraints
1<= T <=10

2<= L<= R<=10^6



Output Format
For each test case, print the maximum difference in the given range in a separate line. 

Sample TestCase 1
Input
5
5 5
2 7
8 10
10 20
4 5
Output
0
5
-1
8
0
Explanation

Test Case 1: [ 5 - 2 ] = 3

Test Case 2: [ 7 - 2 ] = 5

Test Case 3: No prime number in the given range. Output = -1

Test Case 4: [ 19 - 11 ] = 8

Test Case 5: The difference would be 0 since there is only one prime number in the given range.



n=int(input())
def my_function(x):
  return list(dict.fromkeys(x))

def is_prime(n):  
    if n<=1:  
        return False
    for i in range(2,n):
        
        if (n % i) == 0:  
            return False 
        
    return True
li=[]
for i in range(n):
    a=list(map(int,input().split()))
    li.append(a)

for i in li:
    c=i[0]
    d=i[1]
    l=[]
    for num in range(c,d+1):
        if is_prime(num):
            l.append(num)
        
    r = my_function(l)

    if len(r)==0:
        print(-1)
    elif len(r)==1:
        print(0)
    else:
        print(max(r)-min(r))


--------------------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def main():
    testCase = int(input())
    def isprime(n):
        if n<=1:
            return False
        for i in range(2,n):
            if n%i == 0:
                return False
        return True

    while testCase>0:
        LR = list(map(int,input().strip().split()))
        lst=[]
        first = LR[0]
        last = LR[1]
        for i in  range(first,last+1):
            if isprime(i):
                lst.append(i)
                break
            else:
                i=i+1
        for i in range(last,first,-1):
            if isprime(i):
                lst.append(i)
                break
            else:
                i=i+1



        n=len(lst)
        if n>1:
            print(max(lst)-min(lst))
        elif n==1:
            print(0)
        else:
            print(-1)

        testCase -=1
main()
