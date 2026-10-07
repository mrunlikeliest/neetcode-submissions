class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #lowestprice= 0
        #bestprofit = 0
        ans, mi = 0, prices[0]
        for v in prices:
            ans = max(ans, v - mi)
            mi = min(mi, v)
        return ans

        