import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n>0:
            return True if math.log(n,3)-int(math.log(n,3))==0 else False
        else:
            return False

      
