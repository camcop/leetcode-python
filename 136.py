class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        out = set()

        for n in nums:
            if n not in out:
                out.add(n)
            else:
                out.remove(n)

        return out.pop()

