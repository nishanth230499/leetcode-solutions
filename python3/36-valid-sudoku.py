class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if num in rows[i]:
                    return False
                else:
                    rows[i].add(num)
                
                if num in cols[j]:
                    return False
                else:
                    cols[j].add(num)
                
                box = (i//3)*3 + (j//3)
                if num in boxes[box]:
                    return False
                else:
                    boxes[box].add(num)
        
        return True

        