class Solution:
    def rotateString(self, s: str, goal: str):
        n=0
        for n in range(len(s)):
            s = s + s[0]
            s = s[1:]
            print(s)
            if s == goal:
                return True
        return False

s = Solution()
print(s.rotateString('abcde', 'cdeab'))