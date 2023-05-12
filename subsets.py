'''
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example -
Input: nums = [1,2,3]
Output:  [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
'''

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # set a var equal to the length of the list
        n = len(nums)
        # create a list in a list
        output = [[]]
        
        # iterate through nums
        for num in nums:
            # add the new list items as you iterate through output
            output += [curr + [num] for curr in output]
        
        return output