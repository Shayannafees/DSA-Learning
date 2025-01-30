from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int: # type: ignore
        count = 0
        for i in nums:
            if i < k:
                count +=1
        return count

s = Solution()
print(s.minOperations([1,1,2,4,9], 9))