class Solution:
    def largestNumber(self, nums): 
        # if not any(map(bool, nums)):                  handling inp:[0,0,0] => out:0
        #     return '0'
            
        nums = list(map(str, nums)) 


        def compare(i,j):
            return int(nums[i]+nums[j]) > int(nums[j]+nums[i]) 


        for i in range(len(nums)-1):
            j = i + 1
            while i < len(nums) and j < len(nums):
                if compare(i,j):
                    pass
                else:
                    nums[j], nums[i] = nums[i], nums[j]
                j +=1

        return str(int(''.join(nums)))      #str(int('.join(nums))) -> means out will joined by '' 
                                            #then make it int if there any 2 zeros so it'll make it 
                                            # #one, then make it str as it is required to return str output.
    

s = Solution()
print(s.largestNumber([3,30,34,5,9]))
print(s.largestNumber([0,0]))