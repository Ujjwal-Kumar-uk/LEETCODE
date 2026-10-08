def contains_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                return True
    return False
nums = [1,2,3,5,4]
print(contains_duplicate(nums))