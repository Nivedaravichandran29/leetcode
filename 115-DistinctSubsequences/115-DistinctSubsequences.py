# Last updated: 9/24/2026, 9:58:45 PM
1from collections import defaultdict, deque
2
3class Solution:
4    def findLadders(self, beginWord, endWord, wordList):
5        wordSet = set(wordList)
6
7        if endWord not in wordSet:
8            return []
9
10        parents = defaultdict(list)
11        level = {beginWord}
12        found = False
13
14        while level and not found:
15            nextLevel = set()
16
17            for word in level:
18                for i in range(len(word)):
19                    for c in "abcdefghijklmnopqrstuvwxyz":
20                        newWord = word[:i] + c + word[i + 1:]
21
22                        if newWord in wordSet and newWord not in parents:
23                            nextLevel.add(newWord)
24                            parents[newWord].append(word)
25
26                        elif newWord in nextLevel:
27                            parents[newWord].append(word)
28
29                        if newWord == endWord:
30                            found = True
31
32            wordSet -= nextLevel
33            level = nextLevel
34
35        if not found:
36            return []
37
38        result = []
39        path = [endWord]
40
41        def backtrack(word):
42            if word == beginWord:
43                result.append(path[::-1])
44                return
45
46            for parent in parents[word]:
47                path.append(parent)
48                backtrack(parent)
49                path.pop()
50
51        backtrack(endWord)
52
53        return result