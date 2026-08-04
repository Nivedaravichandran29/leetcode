// Last updated: 8/4/2026, 9:27:50 AM
1class Solution {
2public:
3    void nextPermutation(vector<int>& nums) {
4        if(!next_permutation(nums.begin(), nums.end())) {
5            sort(nums.begin(), nums.end());
6        }
7    }
8};