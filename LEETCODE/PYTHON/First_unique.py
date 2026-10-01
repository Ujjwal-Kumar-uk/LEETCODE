def first_unique(s):
    count = {}
    for ch in s:
        if ch in count:
            count[ch]+=1
        else:
            count[ch] = 1
    for i in range(len(s)):
        if count[s[i]] == 1:
            return i
    return -1
s = input("Enter the string: ")
print(first_unique(s))