class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashset =Counter(nums).most_common(k)
        #print(hashset)
        #hashset = {}
        return([val for val, cnt in hashset])
        
        