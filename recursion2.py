'''
Find the maximum value in a given Bitonic array. An array is considered bitonic 
if it is monotonically increasing and then monotonically decreasing. 
Monotonically increasing or decreasing means that for any index i in the 
array arr[i] != arr[i+1]

ex:
Input: [1, 3, 8, 12, 4, 2]
Output: 12
Explanation: The maximum number in the input bitonic array is '12'.

assume that the array is not empty
'''

'''
Pseudocode

base case will check if the length of the list is 1
return that value it is
else
set a value for the max and go to the next num
return the greatest max
'''

def maxVal(nums: list) -> int:
    if len(nums) == 1: # base case
      return nums[0]
    else:
        max = maxVal(nums[1:]) # iterate through list
        return max if max > nums[0] else nums[0] #get greatest val
  
if __name__ == '__main__':
   print(maxVal([1, 3, 8, 12, 4, 2]))