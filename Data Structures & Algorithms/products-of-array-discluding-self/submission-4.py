class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] *len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i]= prefix
            #print(res)
            prefix *= nums[i]
            #print(prefix)
        suff = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suff
            #print (res)
            suff *= nums[i]
        return res