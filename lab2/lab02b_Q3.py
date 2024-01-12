import math
#Q3
def validint():
    while True:
        try:
            n = int(input())
            break
        except ValueError:
            print("Please re-enter:")
    return n
a = validint()
print(bin(a)[2:])
#Q3-3 giống Q1-1
def sum(n):
    sum =0
    for i in range(n):
        sum +=i
    return sum
n = int(input())
b = sum(n)
print(b)
#Q3-4
def reversenumber(n):
    m = 0
    while n>1:
        temp = n%10
        m = m*10 + temp
        n //= 10
    return m
print(reversenumber(n))  
