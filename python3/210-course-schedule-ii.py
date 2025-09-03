class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = {i: set() for i in range(numCourses)}
        for p in prerequisites:
            pre[p[0]].add(p[1])

        visited = set()
        res = []
        current_cycle = set()
        def dfs(i):
            if i in current_cycle:
                return False
            if i in visited:
                return True
            current_cycle.add(i)
            for course in pre[i]:
                if not dfs(course):
                    return False
            visited.add(i)
            res.append(i)
            current_cycle.remove(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res