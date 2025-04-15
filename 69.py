class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        min = 0
        max = x
        
        while True:
            if max == min + 1:
                return min
            mid = (max + min) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                max = mid
            if mid * mid < x:
                min = mid
        

sol = Solution()
print(sol.mySqrt(6))