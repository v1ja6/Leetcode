class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        total = []
        for customer in accounts:
            amount = 0
            for money in customer:
                amount += money
        
            total.append(amount)

        return max(total)
