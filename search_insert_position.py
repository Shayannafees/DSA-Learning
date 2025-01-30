#Input: nums = [1,3,5,6], target = 5
# Output: 2
'''
Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

'''
'''
class Solution:
    def search(self, ints: list, target): # type: ignore
        for i in range(len(ints)): # type: ignore
            if ints[i] == target: # type: ignore
            
                print(i)  # type: ignore
                break



s = Solution()
print(s.search([1,2,3,4,5], 3)) # type: ignore '''


class Solution:
    def search(self, ints: list, target):
        for i in range(len(ints)):
            if ints[i] == target:
                return i
                break
            elif target > ints[-1]:
                return len(ints)
            elif target > ints[i]:
                continue
            elif target < ints[i]:
                return i 
                break


s = Solution()
print(s.search([1,3,5,6], 7))