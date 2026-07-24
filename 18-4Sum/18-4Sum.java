// Last updated: 7/24/2026, 10:23:07 AM
1class Solution {
2    public ListNode reverseKGroup(ListNode head, int k) {
3        ListNode dummy = new ListNode(0);
4        dummy.next = head;
5
6        ListNode prevGroup = dummy;
7
8        while (true) {
9            ListNode kth = prevGroup;
10
11            for (int i = 0; i < k && kth != null; i++) {
12                kth = kth.next;
13            }
14
15            if (kth == null) {
16                break;
17            }
18
19            ListNode groupNext = kth.next;
20            ListNode prev = groupNext;
21            ListNode curr = prevGroup.next;
22
23            while (curr != groupNext) {
24                ListNode temp = curr.next;
25                curr.next = prev;
26                prev = curr;
27                curr = temp;
28            }
29
30            ListNode temp = prevGroup.next;
31            prevGroup.next = kth;
32            prevGroup = temp;
33        }
34
35        return dummy.next;
36    }
37}