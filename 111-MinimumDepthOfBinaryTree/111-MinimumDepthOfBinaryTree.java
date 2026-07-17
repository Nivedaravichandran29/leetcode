// Last updated: 7/17/2026, 3:07:58 PM
class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        // If left subtree is missing
        if (root.left == null) {
            return 1 + minDepth(root.right);
        }

        // If right subtree is missing
        if (root.right == null) {
            return 1 + minDepth(root.left);
        }

        // Both subtrees exist
        return 1 + Math.min(minDepth(root.left), minDepth(root.right));
    }
}