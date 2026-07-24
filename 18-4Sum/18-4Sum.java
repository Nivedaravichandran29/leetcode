// Last updated: 7/24/2026, 10:24:02 AM
1class Solution {
2    public int strStr(String haystack, String needle) {
3        int n = haystack.length();
4        int m = needle.length();
5
6        for (int i = 0; i <= n - m; i++) {
7            int j = 0;
8
9            while (j < m && haystack.charAt(i + j) == needle.charAt(j)) {
10                j++;
11            }
12
13            if (j == m) {
14                return i;
15            }
16        }
17
18        return -1;
19    }
20}