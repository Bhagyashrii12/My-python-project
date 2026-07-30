from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])
        leftToRight = True

        while queue:
            level = []
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                if leftToRight:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)
            leftToRight = not leftToRight

        return result
