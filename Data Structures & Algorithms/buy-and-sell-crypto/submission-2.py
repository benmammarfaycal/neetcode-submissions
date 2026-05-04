class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        max_profit=0
        while right<len(prices):
            if prices[left]>prices[right] and right<len(prices)-1:
                left=right
                right=left+1
            profit=prices[right]-prices[left]
            max_profit=max(max_profit,profit)
            right+=1
        return max_profit
        
