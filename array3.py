'''
Given an array a of n numbers and a count k find the k largest values
in the array a.

ex: a=[5, 1, 3, 6, 8, 2, 4, 7] k=3 => [6, 8, 7]

I will assume that the array will never be empty and that k will always be postive 
and not larger than the length of the array
'''

'''
Pseudocode
sort the given array
return the last k elements of the array
'''

def findLargestValues(a: list, k: int) -> list:
    a.sort() # sort the list from smallest to largest value
    starting_range = len(a) - k #create a range variable to find the last k values
    return a[starting_range:]

if __name__ == "__main__":
    print(findLargestValues([5, 1, 3, 6, 8, 2, 4, 7], 3))
    