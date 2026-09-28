def daily_temp(t,n):
    stack = []
    result = [0]*len(t)
    for i in range(len(t)):
        while stack and t[i] > t[stack[-1]]:
            prev = stack.pop()
            result[prev] = i-prev
        stack.append(i)
    return result
t = []
n = int(input("Enter the size of array: "))
for i in range(n):
    element = int(input())
    t.append(element)
print(daily_temp(t,n))