class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]: 
        l=[]
        for i in arr:
            l += [(bin(i).count('1'), i)]
        l.sort()
        ans=[]
        for i in l:
            ans.append(i[1])
        return(ans)