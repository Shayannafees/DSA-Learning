from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool: # type: ignore
        five = 0
        ten = 0

        for i in bills:
            if i == 5:
                five += 1
            if i == 10:
                ten  += 1
        
            change = i - 5
            if change == 5:
                if five > 0:
                    five -= 1
                else: return False

            if change == 15:
                if five > 0 and ten > 0:
                    five -=1
                    ten -=1
                elif five >= 3:
                    five -= 3
                else: return False
        
        return True


s = Solution()
print(s.lemonadeChange([5,5,10,10,20]))