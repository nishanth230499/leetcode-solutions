class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        profit_sorted = [(item[0], item[1]) for item in items]
        profit_sorted.sort(reverse = True)

        seen_category = set()
        total_profit = 0
        res = 0
        q = []

        for profit, category in profit_sorted:
            if category not in seen_category:
                seen_category.add(category)
            else:
                heapq.heappush(q, profit)
            total_profit += profit

            if len(seen_category) + len(q) > k:
                if q:
                    total_profit -= heapq.heappop(q)        
                else:
                    return res
            res = max(res, total_profit + len(seen_category) ** 2)
        
        return res
