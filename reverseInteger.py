class Solution:
    def reverse(self, x: int) -> int:
        if(x>(-2**31) and x<((2**31)-1)):
            if(x<0):
                x=x*(-1)
                return (self.rev(x))*(-1)
            else:
                return self.rev(x)
        else:
            return 0

    def rev(self,x):
        a=0
        while(x):
            a=(a*10) + (x%10)
            x=x//10
        if((a>(-2**31) and a<((2**31)-1))):
            return a
        else:
            return 0
