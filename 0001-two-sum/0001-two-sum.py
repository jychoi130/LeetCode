class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            ans = []
            a = target - i
            try :
                if nums.index(a, nums.index(i)+1):
                    ans.append(nums.index(i))
                    ans.append(nums.index(a,nums.index(i)+1))
                    return ans
            except : continue