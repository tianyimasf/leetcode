class Solution(object):
    def maxProfitQuick(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        lowest_buy_day = float('inf')
        for buy in prices:
            if buy < lowest_buy_day:
                lowest_buy_day = buy
            if buy - lowest_buy_day > profit:
                profit = buy - lowest_buy_day
        return profit
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i, buy in enumerate(prices[:-1]):
            options = price[i+1:]
            sell = max(options)
            this_profit = sell - buy
            if this_profit > profit:
                profit = this_profit
        return profit

