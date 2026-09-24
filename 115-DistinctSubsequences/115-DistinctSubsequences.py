# Last updated: 9/24/2026, 10:40:23 PM
1class Solution:
2    def countSegments(self, s):
3        count = 0
4
5        for i in range(len(s)):
6            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
7                count += 1
8
9        return count