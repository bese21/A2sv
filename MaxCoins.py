class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        coinsum=0
        piles.sort()
        for i in range(len(piles)//3,len(piles),2):
            coinsum+=piles[i]
        return coinsum
        
