class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            lookup = target - num
            if lookup in hashmap.keys():
                return [hashmap[lookup], index]
            else:
                hashmap[num] = index
        
