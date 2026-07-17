// Last updated: 7/17/2026, 3:07:49 PM
class Solution {
    private int maxPath = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        calculateMaxGain(root);
        return maxPath;
    }

    private int calculateMaxGain(TreeNode node) {
        if (node == null) {
            return 0;
        }

        int leftGain = Math.max(calculateMaxGain(node.left), 0);
        int rightGain = Math.max(calculateMaxGain(node.right), 0);

        int currentPathSum = node.val + leftGain + rightGain;
        maxPath = Math.max(maxPath, currentPathSum);

        return node.val + Math.max(leftGain, rightGain);
    }
}