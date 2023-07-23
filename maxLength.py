class Solution:
    def maxLength(self, arr):
        n = len(arr)

        def backtrack(idx,path):
            if path and len(set(path)) == len(path): res.append(path)

            for i in range(idx,n):
                backtrack(i+1,path+arr[i])

        res = []
        backtrack(0,"")
        return max([len(i) for i in res]) if res else 0


        
        
        
        
