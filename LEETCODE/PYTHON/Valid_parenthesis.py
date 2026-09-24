
def isValid(s):
    stack = []

    for ch in s:
        if ch == '(':
            stack.append(')')
        elif ch == '[':
            stack.append(']')
        elif ch == '{':
            stack.append('}')
        else:
            if len(stack) == 0:
                return False

            if stack.pop() != ch:
                return False

    if len(stack) == 0:
        return True

    return False
s = input("Enter the ch: ")
print(isValid(s))