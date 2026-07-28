class Solution:
    def restoreIpAddresses(self, s):
        res = []

        def backtrack(index, path):
            if len(path) == 4:
                if index == len(s):
                    res.append(".".join(path))
                return

            for i in range(1, 4):
                if index + i > len(s):
                    break

                part = s[index:index + i]

                # Leading zero check
                if len(part) > 1 and part[0] == '0':
                    continue

                # Value must be <= 255
                if int(part) > 255:
                    continue

                path.append(part)
                backtrack(index + i, path)
                path.pop()

        backtrack(0, [])
        return res
