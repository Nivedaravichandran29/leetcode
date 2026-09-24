# Last updated: 9/24/2026, 10:03:50 PM
1class Solution:
2    def minCut(self, s):
3        n = len(s)
4
5        palindrome = [[False] * n for _ in range(n)]
6
7        for i in range(n):
8            palindrome[i][i] = True
9
10        for length in range(2, n + 1):
11            for i in range(n - length + 1):
12                j = i + length - 1
13
14                if s[i] == s[j]:
15                    if length == 2:
16                        palindrome[i][j] = True
17                    else:
18                        palindrome[i][j] = palindrome[i + 1][j - 1]
19
20        dp = [0] * n
21
22        for i in range(n):
23            if palindrome[0][i]:
24                dp[i] = 0
25            else:
26                dp[i] = i
27
28                for j in range(1, i + 1):
29                    if palindrome[j][i]:
30                        dp[i] = min(dp[i], dp[j - 1] + 1)
31
32        return dp[n - 1]