def Erpn(l):
    stack = []
    for ch in l:
        if ch=="+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a+b)
        elif ch=="-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a-b)
        elif ch=="*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a*b)
        elif ch=="/":
            b = stack.pop()
            a = stack.pop()
            stack.append(int(a/b))
        else:
            stack.append(int(ch))
            
    return stack[0]

l = input("Enter the postfix expression: ").split()
print(Erpn(l))