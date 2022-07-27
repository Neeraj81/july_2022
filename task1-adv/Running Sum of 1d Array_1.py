class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=[]
        x=0
        for i in nums:
            x=x+i
            l.append(x)
        return l