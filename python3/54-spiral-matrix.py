class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        v = [[False for _ in matrix[0]] for _ in matrix]
        res = []
        position = [0, 0]
        direction = [0, 1]
        def change_dir(d):
            return [d[1], -d[0]]
        
        def move(p, d):
            return [p[0]+d[0], p[1]+d[1]]
        
        def check_pos(p):
            return 0 <= p[0] < len(matrix) and 0 <= p[1] < len(matrix[0])
        
        while True:
            res.append(matrix[position[0]][position[1]])
            v[position[0]][position[1]] = True
            new_pos = move(position, direction)
            if check_pos(new_pos) and not v[new_pos[0]][new_pos[1]]:
                position = new_pos
                continue
            direction = change_dir(direction)
            new_pos = move(position, direction)
            if check_pos(new_pos) and not v[new_pos[0]][new_pos[1]]:
                position = new_pos
                continue
            break
        
        return res