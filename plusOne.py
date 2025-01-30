from typing import List


class Solution:
    
    def plusOne(self, digits: List[int])-> List[int]: # type: ignore
        a = map(str, digits)
        b = ''.join(a)
        c = int(b)
        print(c)
        res = c+1
        print(res)
        new = str(res)
        new1 = [int(i) for i in new]
        print(new1)
        

s = Solution()
s.plusOne([1,2,3])