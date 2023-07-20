class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)
        nums.sort()
        c=0

        for i in nums:
            if i!=c:
                return c
            c+=1
        else:
            return c
