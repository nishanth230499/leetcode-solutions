from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = []
        pending_groups = defaultdict(list)

        for i, group_size in enumerate(groupSizes):
            pending_groups[group_size].append(i)
            if len(pending_groups[group_size]) == group_size:
                groups.append(pending_groups[group_size])
                pending_groups[group_size] = []
        
        return groups