class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        pairs=[]
        start=0
        end=len(nums)-1
        nums.sort()
        for i in range(len(nums)//2):
                pairs.append(nums[start]+nums[end])
                start+=1
                end-=1
        return max(pairs)
