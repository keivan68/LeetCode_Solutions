class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        dic = {}
        for i,item in enumerate(nums):
            if item not in dic:
                dic[item] = 1
             
        j = 1
        while True:
            if j not in dic:
                return j
            j+=1
