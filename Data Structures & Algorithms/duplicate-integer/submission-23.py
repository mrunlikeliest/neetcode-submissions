class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        asc = sorted(nums)
        for i in range(len(asc)-1):
            if asc[i] == asc[i+1]:
                return True
            
        return False
        
            