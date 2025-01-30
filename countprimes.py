class Solution:
    def countPrimes(self, n: int) -> int: # type: ignore
        if n < 2:
            return 0
        
        count = 0

        for i in range(2,n+1):
            is_prime = True

            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                count +=1
            
        return count
    
s = Solution()
print(s.countPrimes(2))








s = Solution()
s.countPrimes(10)