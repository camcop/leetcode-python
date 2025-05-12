from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        int_index = {}

        for i, n in enumerate(nums):
            if n in int_index:
                if abs(int_index[n] - i) <= k:
                    return True
            int_index[n] = i
            
        return False


                
if __name__=="__main__":
    nums = [1,2,3,1,2,3]
    k = 2
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, 2))

