class Solution:
    def search(self, nums: list[int], target: int) -> int: # type: ignore
        left = 0
        right = len(nums) -1

        while left <= right:
            mid = (left + right)//2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return -1

s = Solution()
print(s.search([-1,0,3,5,9,12], 9)) # type: ignore