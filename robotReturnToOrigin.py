'''Example 1:

Input: moves = "UD"
Output: true
Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
Example 2:

Input: moves = "LL"
Output: false
Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.'''



class Solution:
    def judgeCircle(self, moves: str) -> bool: # type: ignore
        U,L = 1,1
        D,R = -1,-1
        count = 0
        for i in moves:
            if i == U or i == L:
                count += 1
            else:
                count -=1

        return count == 0
    
s = Solution()
print(s.judgeCircle('UD'))