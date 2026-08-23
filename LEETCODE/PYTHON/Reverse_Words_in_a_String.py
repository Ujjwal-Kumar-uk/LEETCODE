def rotstr(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev
s = input("enter the string: ")
print(rotstr(s))