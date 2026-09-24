# Last updated: 9/24/2026, 10:32:04 PM
1class Solution:
2    def findTheDifference(self, s, t):
3        result = 0
4
5        for ch in s:
6            result ^= ord(ch)
7
8        for ch in t:
9            result ^= ord(ch)
10
11        return chr(result)