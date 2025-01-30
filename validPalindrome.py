class Solution:
    def isPalindrome(self, s:str): 
        sen = s.lower().replace(',','').replace(':','').replace(' ','')
        sen1 = ''.join(char.lower() for char in sen if char.isalnum())
        left = 0
        right = len(sen1) -1
        while left <= right:
            if sen1[left] == sen1[right]:
                left +=1
                right -=1
            else:
                return False
        return True

s = Solution()
print(s.isPalindrome('a man, a plan, a canal: Panama'))
print(s.isPalindrome('a.'))