class Solution:
    def prefixCount(self, words, pref):         
        l = len(pref)
        count = 0
        for i in range(0,len(words)): 
            if pref == words[i][0:l]: 
                count += 1
        return count 

s = Solution()
print(s.prefixCount(['pay','attention','practice','attend'], 'at'))