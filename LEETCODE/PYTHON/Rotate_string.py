def rotate(s,g):
    if len(s) != len(g):
        return False
    for i in range(len(s)):
        if s==g:
           return True
        s = s[1:] + s[0]

s = input("enter the string: ")
g = input("enter the goal string: ")
print(rotate(s,g))