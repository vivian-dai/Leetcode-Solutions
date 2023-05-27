class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:  # noqa: F821
        prices.sort()
        if prices[0] + prices[1] <= money:
            return money - (prices[0] + prices[1])
        else:
            return money
        