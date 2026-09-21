def firstocc(h,n):
    for i in range(len(h)-len(n)+1):
        if h[i:i+len(n)]==n:
            return i
    return -1
h = input("enter the first string:")
n = input("enter the second string: ")
print(firstocc(h,n))
