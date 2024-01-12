def palindromechecker(n):
    a = 0
    b = n
    while n>0:
        temp = n%10
        a = a*10+temp
        n //= 10
    if a == b:
        return True
    else:
        return False
m, n = map(int, input().split())
a =[]
if m >n:
    m, n = map(int, input().split())
else:
    for i in range(m,n+1):
        if palindromechecker(i):
            a.append(i)
print(a)
