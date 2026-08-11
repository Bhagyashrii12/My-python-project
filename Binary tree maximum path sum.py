class Solution:
    def maxPathSum(self, root):
        self.answer = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            total = node.val + left + right

            self.answer = max(self.answer, total)

            return node.val + max(left, right)

        dfs(root)

        return self.answer
