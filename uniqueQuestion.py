# The Bermuda Triangle aka the Devil's Triangle, is notoriusly known for being the location
# of many ship and aircraft dissappearances. In this problem, you will explore the Bermudas
# to find the missing item in the Bermuda Triangle.


'''
Directions - Given an array of arrays, return the item within the Bermuda Triangle.
Return False if not found.

Constraints: Triangle base length = 5, Triangle height = 3, len(bermudas) >= 3, 
len(array in bermudas) >= 5, assume only one base can be present

Examples
Given: bermudas = [[3, 5, 6, 2, 4],
                   [5, 6, 1, 6, 3],
                   [6, 6, 6, 6, 6]]

Output: 1

Given: bermudas = [[3, 5, 2, 4, 5, 7, 9, 3, 2],
                   [1, 8, 5, 3, 2, 4, 2, 4],
                   [3, 5, 3, 8, 3, 7, 6, 5, 2, 4],
                   [4, 3, 3, 3, 3, 3, 7, 5, 3,],
                   [7, 8, 3, 1, 1, 1, 4],
                   [5, 4, 2, 1, 6, 7, 7, 3, 2, 2, 7]]

Output: 8

Given: bermudas =  [[3, 5, 2, 4, 5, 7, 9, 3, 2],
                   [1, 3, 5, 6, 2, 4, 2, 4],
                   [3, 5, 7, 8, 6, 3, 6, 5, 2, 4],
                   [3, 3, 6, 4, 6, 6, 7, 5, 3,],
                   [7, 8, 3, 1, 1, 1, 4],
                   [5, 4, 2, 1, 6, 7, 7, 3, 2, 2, 7]]

Output: False

'''
def findItemInBermuda(bermudas: list[list]):
    # find triangle base
    for layer in bermudas:
        count = 0
        for idx, val in enumerate(layer):
            pass
