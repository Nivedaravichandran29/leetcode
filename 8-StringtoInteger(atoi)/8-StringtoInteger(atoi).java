// Last updated: 7/24/2026, 10:18:45 AM
1class Solution {
2    public int myAtoi(String s) {
3        int i = 0;
4        int n = s.length();
5
6        // Step 1: Skip leading whitespaces
7        while (i < n && s.charAt(i) == ' ') {
8            i++;
9        }
10
11        // Step 2: Check sign
12        int sign = 1;
13        if (i < n && (s.charAt(i) == '+' || s.charAt(i) == '-')) {
14            if (s.charAt(i) == '-') {
15                sign = -1;
16            }
17            i++;
18        }
19
20        // Step 3: Convert digits
21        long num = 0;
22        while (i < n && Character.isDigit(s.charAt(i))) {
23            num = num * 10 + (s.charAt(i) - '0');
24
25            // Handle overflow
26            if (sign * num > Integer.MAX_VALUE) {
27                return Integer.MAX_VALUE;
28            }
29            if (sign * num < Integer.MIN_VALUE) {
30                return Integer.MIN_VALUE;
31            }
32
33            i++;
34        }
35
36        return (int) (sign * num);
37    }
38}