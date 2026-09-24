# Last updated: 9/24/2026, 10:48:36 PM
1from collections import deque
2
3class MyStack:
4
5    def __init__(self):
6        self.q1 = deque()
7        self.q2 = deque()
8
9    def push(self, x):
10        self.q2.append(x)
11
12        while self.q1:
13            self.q2.append(self.q1.popleft())
14
15        self.q1, self.q2 = self.q2, self.q1
16
17    def pop(self):
18        return self.q1.popleft()
19
20    def top(self):
21        return self.q1[0]
22
23    def empty(self):
24        return len(self.q1) == 0