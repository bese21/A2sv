import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n>0:
            return True if math.log(n,4)-int(math.log(n,4))==0 else False
        else:
            return False

      
