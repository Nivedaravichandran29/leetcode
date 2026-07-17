// Last updated: 7/17/2026, 3:07:56 PM
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        // If tree is empty
        if (root == null) {
            return false;
        }

        // Check if it's a leaf node
        if (root.left == null && root.right == null) {
            return targetSum == root.val;
        }

        // Recur for left and right subtrees
        return hasPathSum(root.left, targetSum - root.val) ||
               hasPathSum(root.right, targetSum - root.val);
    }
}