class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ll=[]
        l=nums[:n]
        r=nums[n:]
        for i in range(n):
            ll.append(l[i])
            ll.append(r[i])
        return ll