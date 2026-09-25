def two_sum(n,t):

    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if n[i] + n[j] == t:
                return [i,j]
n = int(input("Enter the size: "))
l = []
for i in range(n):
    e = int(input(""))
    l.append(e)
t = int(input("Enter the target: "))
print(two_sum(l,t))

