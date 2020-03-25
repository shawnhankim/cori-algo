"""
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1: return s
        
        s2 = ""
        for i in range(n):
            for j in range(i+1, n+1):
                s1 = s[i:j]
                if s1 == s1[::-1] and len(s1) > len(s2):
                    s2 = s1
        return s2
    
