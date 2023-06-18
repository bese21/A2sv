class Solution:
    def fib(self, n: int) -> int:
        arr=[]
        arr.append(0)
        arr.append(1)
        i=2
        while i <=n:
            arr.append(arr[i-2]+arr[i-1])
            i=i+1
        return arr[n]
            
