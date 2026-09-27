def ispalindrome(s):
    rev = 0
    t = s
    while t>0:
        d = t%10
        rev = rev*10+d
        t = t//10
    return rev == s 

s = int(input("Enter the number: "))
print(ispalindrome(s))