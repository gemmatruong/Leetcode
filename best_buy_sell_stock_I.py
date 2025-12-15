from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

def main():
    sol = Solution()

    print("TEST CASES FOR maxProfit:")

    # 1. Empty list
    prices1 = []
    print(sol.maxProfit(prices1))   # Expected: 0

    # 2. Single day
    prices2 = [5]
    print(sol.maxProfit(prices2))   # Expected: 0

    # 3. Prices always increasing
    prices3 = [1, 2, 3, 4, 5]
    print(sol.maxProfit(prices3))   # Expected: 4

    # 4. Prices always decreasing
    prices4 = [5, 4, 3, 2, 1]
    print(sol.maxProfit(prices4))   # Expected: 0

    # 5. One clear profit opportunity
    prices5 = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(prices5))   # Expected: 5

    # 6. Buy late, sell later
    prices6 = [3, 3, 5, 0, 0, 3, 1, 4]
    print(sol.maxProfit(prices6))   # Expected: 4

    # 7. Buy on first day, sell on last
    prices7 = [2, 4, 1, 7]
    print(sol.maxProfit(prices7))   # Expected: 6

    # 8. Multiple dips
    prices8 = [10, 8, 6, 7, 5, 9]
    print(sol.maxProfit(prices8))   # Expected: 4

    # 9. Large values
    prices9 = [100000, 1, 100000]
    print(sol.maxProfit(prices9))   # Expected: 99999

    # 10. All same prices
    prices10 = [4, 4, 4, 4]
    print(sol.maxProfit(prices10))  # Expected: 0


if __name__ == "__main__":
    main()
