def isomorphic_string(s,t):
    m1 = {}
    m2 = {}
    for i in range(len(s)):
        a = s[i]
        b = t[i]
        if a in m1 and m1[a] != b:
            return False
        if b in m2 and m2[b] != a:
            return False
        m1[a] = b
        m2[b] = a
    return True
s = input("Enter First string: ")
t = input("Enter Second string: ")
print(isomorphic_string(s,t))
