from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        half = len(nums)//2
        for i in range(0,half): # type: ignore
            sum_of_3 = sum(nums[i:i+2])
            min = sum_of_3
        return min

    
s = Solution()
print(s.threeSumClosest([-1,2,1,-4], 1))