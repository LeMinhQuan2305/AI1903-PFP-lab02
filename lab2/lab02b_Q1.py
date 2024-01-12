import math
#Q1 - 1
def ninput():              #hàm Q1-1
    n = int(input())
    if n <= 5:
        return ninput()
    else: 
        return n
def suminput(n, S1=0):    #hàm Q1-2
    for i in range(n):
        S1 +=i
    return S1
def Q13(n, S2= 1):     #hàm Q1-3
    for i in range(1, n):
        S2 *= i
    return S2
def Q14(n, S3 = 0):    #hàm Q1-4
    for i in range(1, n):
        S3 += i**-1
    return S3
def primeinputchecker():          #hàm Q1-5
    n = int(input())
    if n <2:
        return "Not a prime number"
    elif n==2:
        return "Prime number"
    else:
        for i in range(2, n):
            if n%i == 0:
                return "Not a prime number"
        return "Prime number"
            
a = ninput()
print(a)
print(suminput(a))
print(Q13(a))
print(Q14(a))
b = primeinputchecker()
print(b)


##############################################################################
