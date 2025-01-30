class Solution:
    def rotateString(self, s: str, goal: str) -> bool: # type: ignore
        a = list(s)
        for n in a:
            n = 0
            m = a.pop(n) # type: ignore
            o = a.append(m)
            x = ''.join(a)
            if x == goal:
                return True
                break
            else:
                x = a
        return False

s = Solution()
s.rotateString('abcde', 'cdeab')