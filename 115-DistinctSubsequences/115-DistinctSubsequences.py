# Last updated: 9/24/2026, 10:28:21 PM
1class Solution:
2    def reverseString(self, s):
3        left = 0
4        right = len(s) - 1
5
6        while left < right:
7            s[left], s[right] = s[right], s[left]
8            left += 1
9            right -= 1