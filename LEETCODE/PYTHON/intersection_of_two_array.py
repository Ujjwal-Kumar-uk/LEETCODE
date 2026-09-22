def inter(a,b):
    count = {}
    result = []
    for i in a:
        if i in count:
            count[i]+=1
        else:
            count[i]=0
    for i in b:
        if i in count and count[i]>0:
            result.append(i)

    return result
a = [4,4,5]
b = [4]
print(inter(a,b))