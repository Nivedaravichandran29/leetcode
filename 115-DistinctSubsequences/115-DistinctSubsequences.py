# Last updated: 9/24/2026, 10:42:40 PM
1class Solution:
2    def repeatedSubstringPattern(self, s):
3        n = len(s)
4
5        for length in range(1, n):
6            if n % length == 0:
7                pattern = s[:length]
8
9                if pattern * (n // length) == s:
10                    return True
11
12        return False