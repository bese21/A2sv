class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        helper=collections.Counter(nums)
        elements = helper.most_common(k)
        result = []
        for tup in elements:
            result.append(tup[0])
        return result
        
        
