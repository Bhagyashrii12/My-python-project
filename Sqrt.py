class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0

        left = 1
        right = x
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
