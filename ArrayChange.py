class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index_map = {v: i for i, v in enumerate(nums)}
        for v in operations:
            index = index_map[v[0]]
            nums[index] = v[1]
            index_map[v[0]] = -1 
            index_map[v[1]] = index
        return nums
