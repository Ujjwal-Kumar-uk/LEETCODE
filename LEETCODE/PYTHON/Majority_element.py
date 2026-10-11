def majority(s):
    freq = {}

    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i] = 1
    for i in freq:
        if freq[i] > len(s) //2:
            return i
        
s = [1,1,2,0,2,2,2]
print(majority(s))
       