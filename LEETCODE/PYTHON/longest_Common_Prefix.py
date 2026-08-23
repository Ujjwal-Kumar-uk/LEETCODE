def longComPre(s):
    if len(s)==0:
        return ""
    prefix = s[0]
    for i in range(1,len(s)):
        j = 0
        while j<len(prefix) and j<len(s[i]):
            if prefix[j] != s[i][j]:
                break
            j+=1
        prefix = prefix[:j]

        if prefix=="":
            return ""
    return prefix
s = input("enter the string seperated by space: ").split()
print(longComPre(s))