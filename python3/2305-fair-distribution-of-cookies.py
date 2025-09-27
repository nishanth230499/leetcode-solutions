class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.min_dis = float("inf")
        dis = [0] * k
        def rec(i, max_dis, zero_count):
            if i == len(cookies):
                self.min_dis = min(self.min_dis, max_dis)
            elif len(cookies) - i < zero_count:
                return
            else:
                for j in range(k):
                    dis[j] += cookies[i]
                    rec(i + 1, max(max_dis, dis[j]), zero_count-1 if dis[j] == cookies[i] else zero_count)
                    dis[j] -= cookies[i]
        
        rec(0, 0, k)
        return self.min_dis