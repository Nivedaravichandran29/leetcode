// Last updated: 7/24/2026, 10:22:08 AM
1class Solution {
2    public ListNode reverseKGroup(ListNode head, int k) {
3
4        ListNode curr = head;
5        int count = 0;
6
7        // Check if there are at least k nodes
8        while (curr != null && count < k) {
9            curr = curr.next;
10            count++;
11        }
12
13        // If k nodes exist, reverse them
14        if (count == k) {
15            curr = reverseKGroup(curr, k);
16
17            while (count-- > 0) {
18                ListNode temp = head.next;
19                head.next = curr;
20                curr = head;
21                head = temp;
22            }
23
24            head = curr;
25        }
26
27        return head;
28    }
29}