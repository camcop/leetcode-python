from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        q = []

        for i, n in enumerate(nums):
            if n in q:
                return True
            q.append(n)
            if len(q) > k:
                q.pop(0)
        
        return False


                
if __name__=="__main__":
    nums = [1,2,3,1,2,3]
    k = 2
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, 2))

