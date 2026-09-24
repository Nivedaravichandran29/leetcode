# Last updated: 9/24/2026, 10:33:19 PM
1class Solution:
2    def toHex(self, num):
3        if num == 0:
4            return "0"
5
6        digits = "0123456789abcdef"
7        result = ""
8
9        if num < 0:
10            num += 2**32
11
12        while num > 0:
13            digit = num & 15
14            result = digits[digit] + result
15            num >>= 4
16
17        return result