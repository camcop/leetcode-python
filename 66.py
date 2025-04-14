class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        n = 0
        power = 0
        for d in digits[::-1]:
            n += d * pow(10, power)
            power += 1
        
        n += 1

        digits_incremented = [int(d) for d in str(n)]

        return digits_incremented

        

sol = Solution()
print(sol.plusOne([1, 2, 3]))