'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''
def removeElement(self, nums: list[int], val: int) -> int:
    #set count
    count = 0
    #iterate through items
    for i in range(len(nums)):
        #check if item is equal to val
        if nums[i] != val :
            #if not set nums[count] to nums[i] and increment count by 1
            nums[count] = nums[i]
            count +=1
    return count



'''
Input: nums = [3,2,2,3], val = 3
Output: 2, nums =  [2,2,_,_]
'''
# nums = [3,2,2,3]
# val = 3
# count = 0 

# start iteration
'''
count = 0
i = 0
nums[i] = nums[0] = 3
nums[i] equals 3 (val)
count = 0
nums = [3, 2, 2, 3]
'''

'''
count = 0
i = 1
nums[i] = nums[1] = 2
nums[i] does not equal 3 (2 != 3)
    nums[count] = nums[1]
    nums[0] = 2

count = 1
nums = [2, 2, 2, 3]
'''

'''
count = 1
i = 2
nums[i] = nums[2] = 2
nums[i] does not equal 3 (2 != 3)
    nums[count] = nums[2] 
    nums[1] = 2
    
count = 2
nums = [2, 2, 2, 3]
'''

'''
count = 2
i = 3
nums[i] = nums[3] = 3
nums[i] equals 3 (val)

nums = [2, 2, 2, 3]
'''

# return 2