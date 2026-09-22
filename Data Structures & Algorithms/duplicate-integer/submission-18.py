class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag: int = 0
        asc = sorted(nums)
        for i in range(len(asc)-1):
            if asc[i] == asc[i+1]:
                flag=flag+1
        if flag != 0:
            return True
        else:
            return False
            