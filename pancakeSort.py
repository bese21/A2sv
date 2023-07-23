class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        def sort(node):
            if node == 0:
                return
            
            a = 0
            for i in range(1,node):
                if arr[i-1] >arr[i]:
                    a = i
                    break

            if a == 0:
                return 

            index,max_num = -1,-1
            for i in range(node):
                if arr[i]>max_num:
                    index,max_num = i,arr[i]

            ans.append(index+1)
            arr[:index+1] = arr[:index+1][::-1]
            ans.append(node)
            arr[:node] = arr[:node][::-1]
            sort(node-1)
            

        sort(len(arr))
        return ans
            
            
                    
