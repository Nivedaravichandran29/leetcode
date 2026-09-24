# Last updated: 9/24/2026, 10:45:46 PM
1class Solution:
2    def findWords(self, words):
3        row1 = set("qwertyuiop")
4        row2 = set("asdfghjkl")
5        row3 = set("zxcvbnm")
6
7        result = []
8
9        for word in words:
10            w = word.lower()
11
12            if all(ch in row1 for ch in w):
13                result.append(word)
14            elif all(ch in row2 for ch in w):
15                result.append(word)
16            elif all(ch in row3 for ch in w):
17                result.append(word)
18
19        return result