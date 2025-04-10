class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        unique = set()
        p = 0
        for i, n in enumerate(nums):
            if n not in unique:
                unique.add(n)
                nums[p] = n
                p += 1

        return p