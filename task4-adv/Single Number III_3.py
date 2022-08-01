class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        res=[]
        for i in set(nums):
            d[i]=nums.count(i)
        for i in d:
            if d[i]==1:
                res.append(i)
        return res