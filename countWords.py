class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        a = []
        for i in words1:
            if words1.count(i) == 1 and words2.count(i) == 1:
                    a.append(i)
                    print(a)
        return len(a)


s = Solution()
print(s.countWords(['a','ab'], ['a', 'a', 'a', 'ab']))