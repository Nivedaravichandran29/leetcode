# Last updated: 9/24/2026, 9:52:02 PM
1class Solution:
2    def exist(self, board, word):
3        def backtrack(i, j, k):
4            if k == len(word):
5                return True
6            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
7                return False
8            
9            temp = board[i][j]
10            board[i][j] = ''
11            
12            if backtrack(i+1, j, k+1) or backtrack(i-1, j, k+1) or backtrack(i, j+1, k+1) or backtrack(i, j-1, k+1):
13                return True
14            
15            board[i][j] = temp
16            return False
17        
18        for i in range(len(board)):
19            for j in range(len(board[0])):
20                if backtrack(i, j, 0):
21                    return True
22        return False
23        