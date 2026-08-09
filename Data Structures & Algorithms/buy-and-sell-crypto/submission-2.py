class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxi = 0
        for i in range(len(prices)-1):
            first = i
            last = i+1

            while first < last and last <= len(prices)-1:
                if prices[last]> prices[first]:
                    profit = prices[last]-prices[first]
                    maxi = max(maxi, profit)
                    last+=1
                else:
                    last+=1
                
        return maxi
