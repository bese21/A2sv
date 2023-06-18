class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
      
        counter=0
        for i in range(len(nums)):
            sum1=0
            sum2=0
            for j in range(i+1,len(nums)):
                sum1=sum1+nums[j]
               
            for k in range(0,i):
                sum2=sum2+nums[k]
           
            if sum1==sum2:
                return i
            elif (i==0 and sum1==0 )or (i==len(nums)-1 and sum2==0 ):
                return 0
           
        return -1
     
    
        return 0  
