import math
#Q1 -1

def func2(*args):
    for i in args:
        print(i)
func2(20, 40, 60, 80, 100)
#Q1 - 2
def calc(a,b):
    return a+b, a-b
res = calc(40, 10)
print(res)    
#Q2 - 1
def showEmployee (a, b=9000):
    print("Name: ", a, "Salary: ", b)

showEmployee("Ben", 12000)
showEmployee("Jessa")
# Q2 - 2
def outfunc(a, b):
    def infunc(a, b):
        return a+b
    return infunc(a, b) + 5
result = outfunc(5, 10)
print(result)
# Q3 - 1

def recurfunc(a, i = 0, tong = 0):
    if i <= a:
        tong = tong + i
        i += 1
        return recurfunc(a, i, tong)
    else:
        return tong
res = recurfunc(10)
print(res)
# Q3 - 2
def display_student(name, age):
    print(name, age)
show_student = display_student
show_student("a",2)
# Q4 - 1
def Palindrome(a, b = 0, n = 0):
    while a > 1:
        temp = a%10
        b = temp*pow(10,n)
        n = n+1
        a = a/10
    if b == a:
        return b
    else:
        return b
if Palindrome(252):
    print("is a palindrome number")
else:
    print("isnt a palindrome number")
# Q4 - 2
def max():
    max = 0
    array = list(map(int, input().split()))
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
    return max        
maximum = max()
print(maximum)
    