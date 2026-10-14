def Move_zeros(nums):

    j = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[j] = nums[i]
            j+=1

    while j<len(nums):
        nums[j] = 0
        j+=1
        
    return nums

nums = [0,1,0,2,0,3,4]
print(Move_zeros(nums))
        