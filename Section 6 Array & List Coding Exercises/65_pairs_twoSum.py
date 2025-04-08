def pairs(nums, target):
    listPairs = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target and nums[i] != nums[j]:
                listPairs.append([i, j])
        
    return listPairs

# Test the function
nums = [2, 7, 11, 15]
target = 9
result = pairs(nums, target)
print((result)) 


nums = [0,1,2,3,4,5,6,7,8,9,10]
target = 6
result = pairs(nums, target)
print((result)) 

# The function returns pairs of numbers that add up to the target value.