def valid(s):
    open = 0
    close = 0

    for ch in s:
        if ch=="(":
            open += 1
        else:
            if open>0:
                open -= 1
            else:
                close += 1
    return open+close

s = input("enter the parenthesis:")
print(valid(s))