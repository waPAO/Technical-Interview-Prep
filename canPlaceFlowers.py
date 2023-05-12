# Can Place Flowers
'''
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
'''

'''
Example:
    Input: flowerbed =  [1,0,0,0,1], n = 2
    Output: false
'''
class Solution:
    '''
    Pseudocode

    SET count to 0
    ITERATE over length of flowerbed
        CHECK if flowerbed at index "i" is equal to 0
            check if the left plot is empty
            check if the right plot is empty

            CHECK if both left and right plots are empty
                SET flowerbed at index "i" to 1
                INCREMENT count by 1
    RETURN count is greater than or equal to n
    '''
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_plot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_plot:
                    flowerbed[i] = 1
                    count += 1
                    
        return count >= n
    

'''
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
'''
# First iteration
'''
count = 0
for i in range(5):
    i = 0
    flowerbed[0] = 1, 1 != 0

count = 0
'''
# Second iteration 
'''
count = 0
for i in range(5):
    i = 1
    flowerbed[1] = 0, 0 == 0:
        empty_left_plot = False ((i != 0) or (flowerbed[i-1] != 0))
        empty_right_plot = True (flowerbed[i + 1] == 0)
        
        # does not enter second if statement
        
count = 0
'''
# Third iteration
'''
count = 0
for i in range(5):
    i = 2
    flowerbed[2] = 0, (0 == 0):
        empty_left_plot = True ( (flowerbed[i-1] == 0)
        empty_right_plot = True (flowerbed[i + 1] == 0)
        
        #both plots are empty
        flowerbed[2] = 1
        count += 1
        
count = 1
'''
# Fourth iteration
'''
count = 1
for i in range(5):
    i = 3
    flowerbed[3] = 0, (0 == 0):
        empty_left_plot = False ((i != 0) or (flowerbed[i-1] != 0))
        empty_right_plot = False (i != len(flowerbed) - 1) or (flowerbed[i + 1] != 0)
        
        # does not enter second if statement
        
count = 1
'''
# Final iteration
'''
count = 1
for i in range(5):
    i = 4
    flowerbed[4] = 1, (1 != 0)

        
count = 1
'''
# return 1 >= 2 => False