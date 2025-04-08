class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        unique = set()
        
        operations = 0
        i = 0
        while i < len(nums):
            if len(nums) == 0:
                return operations
            if nums[i] not in unique:
                unique.add(nums[i])
                i += 1
            else:
                nums = nums[3:]
                operations += 1
                i = 0
                unique = set()
        
        return operations

