from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == '':
            return True
    
        for word in wordDict:
            if s.startswith(word):
                remaining = s[len(word):]
                if self.wordBreak(remaining, wordDict):
                    return True
        
        return False







s = Solution()
print(s.wordBreak("leetcode",["leet","code"]))