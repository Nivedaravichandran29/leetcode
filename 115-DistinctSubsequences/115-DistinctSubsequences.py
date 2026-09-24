# Last updated: 9/24/2026, 10:20:17 PM
1class Solution:
2    def addOperators(self, num, target):
3        result = []
4
5        def backtrack(index, expression, value, previous):
6            if index == len(num):
7                if value == target:
8                    result.append(expression)
9                return
10
11            for i in range(index, len(num)):
12                if i > index and num[index] == '0':
13                    break
14
15                current = num[index:i + 1]
16                current_num = int(current)
17
18                if index == 0:
19                    backtrack(
20                        i + 1,
21                        current,
22                        current_num,
23                        current_num
24                    )
25                else:
26                    backtrack(
27                        i + 1,
28                        expression + "+" + current,
29                        value + current_num,
30                        current_num
31                    )
32
33                    backtrack(
34                        i + 1,
35                        expression + "-" + current,
36                        value - current_num,
37                        -current_num
38                    )
39
40                    backtrack(
41                        i + 1,
42                        expression + "*" + current,
43                        value - previous + previous * current_num,
44                        previous * current_num
45                    )
46
47        backtrack(0, "", 0, 0)
48
49        return result