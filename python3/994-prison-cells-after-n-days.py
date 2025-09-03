class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def process(cells):
            new_cells = [0] * len(cells)
            for i in range(1, len(cells) - 1):
                if cells[i-1] == cells[i+1]:
                    new_cells[i] = 1
            return new_cells
        
        if cells[0] == 1 or cells[len(cells) - 1] == 1:
            cells = process(cells)
            n = n - 1
        
        i = 0
        seen = set()
        while True:
            if i == n:
                return cells
            key = ",".join(list(map(str, cells)))
            if key in seen:
                break
            seen.add(key)
            cells = process(cells)
            i += 1
        
        n = n % i
        for i in range(n):
            cells = process(cells)
        return cells
                    