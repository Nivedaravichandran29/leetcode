# Last updated: 9/24/2026, 10:04:51 PM
1class Solution:
2    def wordBreak(self, s, wordDict):
3        wordSet = set(wordDict)
4        memo = {}
5
6        def dfs(start):
7            if start == len(s):
8                return [""]
9
10            if start in memo:
11                return memo[start]
12
13            result = []
14
15            for end in range(start + 1, len(s) + 1):
16                word = s[start:end]
17
18                if word in wordSet:
19                    sentences = dfs(end)
20
21                    for sentence in sentences:
22                        if sentence:
23                            result.append(word + " " + sentence)
24                        else:
25                            result.append(word)
26
27            memo[start] = result
28            return result
29
30        return dfs(0)