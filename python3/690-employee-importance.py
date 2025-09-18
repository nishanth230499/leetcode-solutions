"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        id_index_map = {}
        for i, emp in enumerate(employees):
            id_index_map[emp.id] = i

        def rec(cur):
            emp = employees[id_index_map[cur]]
            res = emp.importance
            for sub in emp.subordinates:
                res += rec(sub)
            return res
        
        return rec(id)
            