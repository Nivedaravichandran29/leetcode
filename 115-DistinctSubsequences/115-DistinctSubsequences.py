# Last updated: 9/24/2026, 10:22:47 PM
1class Solution:
2    def wordPattern(self, pattern, s):
3        words = s.split()
4
5        if len(pattern) != len(words):
6            return False
7
8        char_to_word = {}
9        word_to_char = {}
10
11        for ch, word in zip(pattern, words):
12            if ch in char_to_word:
13                if char_to_word[ch] != word:
14                    return False
15
16            if word in word_to_char:
17                if word_to_char[word] != ch:
18                    return False
19
20            char_to_word[ch] = word
21            word_to_char[word] = ch
22
23        return True