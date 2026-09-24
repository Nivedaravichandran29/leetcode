# Last updated: 9/24/2026, 10:16:42 PM
1class Solution:
2    def shortestPalindrome(self, s):
3        if not s:
4            return ""
5
6        rev = s[::-1]
7
8        for i in range(len(s)):
9            if s[:len(s) - i] == rev[i:]:
10                return rev[:i] + s
11
12        return ""