import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        sorted_dict = sorted(count.items(), key = lambda item: item[1], reverse = True)
        ans = []

        print(count)
        print(sorted_dict)

        for i in range(0,k):
            ans.append(sorted_dict[i][0])
        
        return ans