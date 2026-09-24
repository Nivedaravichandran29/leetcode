# Last updated: 9/24/2026, 10:43:46 PM
1class Solution:
2    def getMaxRepetitions(self, s1, n1, s2, n2):
3        if not set(s2).issubset(set(s1)):
4            return 0
5
6        index = 0
7        count1 = 0
8        count2 = 0
9
10        seen = {}
11
12        while count1 < n1:
13            count1 += 1
14
15            for ch in s1:
16                if ch == s2[index]:
17                    index += 1
18
19                    if index == len(s2):
20                        index = 0
21                        count2 += 1
22
23            if index in seen:
24                prev_count1, prev_count2 = seen[index]
25
26                cycle1 = count1 - prev_count1
27                cycle2 = count2 - prev_count2
28
29                remaining = n1 - count1
30                cycles = remaining // cycle1
31
32                count1 += cycles * cycle1
33                count2 += cycles * cycle2
34
35            else:
36                seen[index] = (count1, count2)
37
38        return count2 // n2