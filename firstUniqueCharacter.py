'''
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.

Examples:
Input: s = "leetcode"
Output: 0

Input: s = "loveleetcode"
Output: 2

Input: s = "aabb"
Output: -1
'''
import collections

# Build hashmap out of list
# Enumerate through given string
# Check at each key if the value is 1
#   Return the index if True
# Return -1 if none are 1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1

'''
Ex:
Input: s = "loveleetcode"
Output: 2



count = Counter({'e': 4, 'l': 2, 'o': 2, 'v': 1, 't': 1, 'c': 1, 'd': 1})

# first iteration
idx = 0
ch = 'l'
count['l'] => 2

# second iteration 
idx = 1
ch = 'o'
count['o'] => 2

#third iteration
idx = 2
ch = 'v'
count['v'] => 1

return 2
'''