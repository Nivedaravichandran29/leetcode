# Last updated: 9/24/2026, 10:34:39 PM
1class Solution:
2    def longestPalindrome(self, s):
3        count = {}
4
5        for ch in s:
6            count[ch] = count.get(ch, 0) + 1
7
8        length = 0
9        has_odd = False
10
11        for freq in count.values():
12            length += (freq // 2) * 2
13
14            if freq % 2 == 1:
15                has_odd = True
16
17        if has_odd:
18            length += 1
19
20        return length