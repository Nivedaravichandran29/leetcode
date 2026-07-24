// Last updated: 7/24/2026, 10:19:59 AM
1import java.util.*;
2
3class Solution {
4    public List<List<Integer>> fourSum(int[] nums, int target) {
5        List<List<Integer>> result = new ArrayList<>();
6
7        Arrays.sort(nums);
8        int n = nums.length;
9
10        for (int i = 0; i < n - 3; i++) {
11
12            // Skip duplicate values for i
13            if (i > 0 && nums[i] == nums[i - 1])
14                continue;
15
16            for (int j = i + 1; j < n - 2; j++) {
17
18                // Skip duplicate values for j
19                if (j > i + 1 && nums[j] == nums[j - 1])
20                    continue;
21
22                int left = j + 1;
23                int right = n - 1;
24
25                while (left < right) {
26
27                    long sum = (long) nums[i] + nums[j] + nums[left] + nums[right];
28
29                    if (sum == target) {
30
31                        result.add(Arrays.asList(
32                                nums[i], nums[j], nums[left], nums[right]));
33
34                        left++;
35                        right--;
36
37                        // Skip duplicates
38                        while (left < right && nums[left] == nums[left - 1])
39                            left++;
40
41                        while (left < right && nums[right] == nums[right + 1])
42                            right--;
43
44                    } else if (sum < target) {
45                        left++;
46                    } else {
47                        right--;
48                    }
49                }
50            }
51        }
52
53        return result;
54    }
55}