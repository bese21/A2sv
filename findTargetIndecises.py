class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        counterlist=[]
        nums.sort()
        for i in range(0,len(nums)):
            if nums[i]==target:
                counterlist.append(i)
        return counterlist
