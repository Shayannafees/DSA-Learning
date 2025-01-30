from typing import List


class Solution:
    def TwoSum(self, nums: List[int], target: int) -> int: # type: ignore
        left,right = 0, len(nums)-1
        sorted_arr = nums.sort()
        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                return [left, right]     # type: ignore
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        # return [] # type: ignore

s = Solution()
print(s.TwoSum([3,2,4], 6))