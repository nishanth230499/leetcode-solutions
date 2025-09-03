class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {i: set() for i in range(numCourses)}
        for p in prerequisites:
            pre[p[0]].add(p[1])

        visited = set()
        current_cycle = set()
        def dfs(i):
            if i in current_cycle:
                return False
            if i in visited:
                return True
            current_cycle.add(i)
            visited.add(i)
            for course in pre[i]:
                if not dfs(course):
                    return False
            current_cycle.remove(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True