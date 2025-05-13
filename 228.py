from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        range_list = []

        range_i = []
        for i, n in enumerate(nums):
            if len(range_i) == 0:
                range_i.append(n)
            # if i == 0:
                # range_i.append(n)
            elif n != nums[i - 1] + 1:
                range_i.append(nums[i - 1])
                range_list.append(range_i)
                range_i = [n]
            if i == len(nums) - 1:
                range_i.append(n)
                range_list.append(range_i)

        out_list = []
        for range_i in range_list:
            if range_i[1] == range_i[0]:
                out_list.append(str(range_i[0]))
            else:
                out_list.append(str(range_i[0]) + "->" + str(range_i[1]))
        
        return out_list




nums = [0,1,2,4,5,7]
sol = Solution()
print(sol.summaryRanges(nums))