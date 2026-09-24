# Last updated: 9/24/2026, 10:41:38 PM
1class Solution:
2    def findAnagrams(self, s, p):
3        if len(p) > len(s):
4            return []
5
6        p_count = [0] * 26
7        window = [0] * 26
8        result = []
9
10        for ch in p:
11            p_count[ord(ch) - ord('a')] += 1
12
13        for i in range(len(s)):
14            window[ord(s[i]) - ord('a')] += 1
15
16            if i >= len(p):
17                window[ord(s[i - len(p)]) - ord('a')] -= 1
18
19            if window == p_count:
20                result.append(i - len(p) + 1)
21
22        return result