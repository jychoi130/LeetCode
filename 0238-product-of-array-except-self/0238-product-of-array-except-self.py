#from math import prod
from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        ans = []
        
        checking = nums.copy()

        for i in range(0,len(nums)):
            check = nums.pop(0)
            if(checking.index(check) != i ):
                ans.append(ans[checking.index(check)])
                mul *= check
                continue
            #multi = prod(nums)
            multi = reduce(lambda x,y:x*y, nums, 1)
            num = multi*mul
            ans.append(num)
            mul *= check
        
        #ans.reverse()

        return ans
            
            
        
