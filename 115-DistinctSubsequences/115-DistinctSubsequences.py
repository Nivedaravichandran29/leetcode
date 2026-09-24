# Last updated: 9/24/2026, 9:57:16 PM
1class Solution:
2    def numDistinct(self, s, t):
3        m = len(s)
4        n = len(t)
5
6        dp = [[0] * (n + 1) for _ in range(m + 1)]
7
8        for i in range(m + 1):
9            dp[i][0] = 1
10
11        for i in range(1, m + 1):
12            for j in range(1, n + 1):
13                if s[i - 1] == t[j - 1]:
14                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
15                else:
16                    dp[i][j] = dp[i - 1][j]
17
18        return dp[m][n]