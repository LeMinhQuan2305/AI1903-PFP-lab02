import math
#Q2-1
def isprime(n):
    if n < 2:
        return False
    elif n==2:
        return True
    else:
        for i in range(2, n):
            if n%i ==0:
                return False
        return True
def primedividers(a, b):    # tìm tất cả các ước chung là số nguyên tố
    smolnumber = min(a,b)
    cpd=[]
    for i in range(1, smolnumber):
        if isprime(i) and a%i ==0 and b%i ==0:
            cpd.append(i)
    return cpd
#Q2-2 
def GCD(a,b): # tìm ước chung lớn nhất
    smolnumber=min(a,b)
    UCLN = 0
    for i in range(1, smolnumber):
        if a%i== 0 and b%i ==0 and i>= UCLN:
            UCLN = i
    return UCLN 
a, b = map(int, input().split())
#Q2-3 : Tìm bội chung nhỏ nhất
def LDM(a,b):
    i = 1
    while i <= a*b:
        if i%a==0 and i%b ==0:
            return i
        else:
            i = i+1
print(primedividers(a, b))
print(GCD(a,b))
print(LDM(a,b))

