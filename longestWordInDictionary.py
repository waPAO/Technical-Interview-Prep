'''
Given an array of strings words representing an English Dictionary,
return the longest word in words that can be built one character at a time 
by other words in words.

If there is more than one possible answer, return the longest word with the smallest
lexicographical order. If there is no answer, return the empty string.

Examples -
Input: words =  ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
'''

class Solution:
    def longestWord(self, words: list[str]) -> str:
        # Create an empty string
        ans = ""
        # Turn your list into a set
        wordset = set(words)
        # Iterate through list
        for word in words:
            # Check each word
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:k] in wordset for k in xrange(1, len(word))):
                    ans = word

        return ans