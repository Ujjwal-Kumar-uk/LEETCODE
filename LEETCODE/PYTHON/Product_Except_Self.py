def productExceptSelf(nums):
    n = len(nums)
    result = [1]*n
    prefix = 1

    for i in range(n):
        result[i] = prefix
        prefix = prefix * nums[i]
    suffix = 1
    for i in range(n-1,-1,-1):
        result[i] = result[i]*suffix
        suffix = suffix*nums[i]
    return result

nums = [1,2,3,4]
print(productExceptSelf(nums))