'''
Given two arrays a and b of numbers and a target value t,
find a number from each array whose sum is closest to t.
Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],
t=20  ⇒  [13, 6] or [4, 17] or [5, 14]
'''

'''
Pseudocode
traverse through both lists with a nested loop
check if for the closest sum
use absolute to check
set the closest sum to new sum
set another var to answer
return
'''

def findMixedSum(a: list, b: list, t: int) -> list:
    check_sum = None #set up vars

    # make nested loop
    for num1 in a:
        for num2 in b:
            check = abs(num1 + num2 - t) #check how close sum is
            if not check_sum or check < check_sum: # check for closest sum
                check_sum = check
                pair = [num1, num2] # assign answer
    return pair

if __name__ == "__main__":
    print(findMixedSum([9, 13, 1, 8, 12, 4, 0, 5], [3, 17, 4, 14, 6], 20))