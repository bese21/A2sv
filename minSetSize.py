
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        d = Counter(arr)
        d = sorted(d.items(), key = lambda x:x[1],reverse=True)
        res, score = 0,0
        for i in d:
            res += 1
            score += i[1]
            if score >= int(n/2):
                return res
        else:
            return 0
