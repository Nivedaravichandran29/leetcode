// Last updated: 8/4/2026, 9:28:30 AM
1class Solution {
2public:
3    int longestValidParentheses(string s) {
4        stack<int> st;
5        st.push(-1);
6        int max_len = 0;
7
8        for (int i = 0; i < s.length(); i++) {
9            if (s[i] == '(') {
10                st.push(i);
11            } else {
12                st.pop();
13                if (st.empty()) {
14                    st.push(i);
15                } else {
16                    max_len = max(max_len, i - st.top());
17                }
18            }
19        }
20
21        return max_len;        
22    }
23};