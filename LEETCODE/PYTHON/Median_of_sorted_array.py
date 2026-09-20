def merge(a,b):
    c = a+b
    c.sort()
    n = len(c)
    if n%2==1:
        return c[n//2]
    else:
        p = c[n//2-1]
        q = c[n//2]
        return p+q

a = []
b = []

a1 = int(input("enter the size of array1: "))
for i in range(0,a1):
    element = int(input())
    a.append(element)

b1 = int(input("Enter the size of array2: "))
for i in range(0,b1):
    element = int(input())
    b.append(element)
print("MEDIAN:",merge(a,b))