class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial_color = image[sr][sc]
        if initial_color == color:
            return image
        dirs = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]

        def rec(i, j):
            if image[i][j] == initial_color:
                image[i][j] = color
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if(0 <= x < len(image) and 0 <= y < len(image[0])):
                        rec(x, y)
        
        rec(sr, sc)
        return image