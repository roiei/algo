

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rect = rectangle
        self.rows = len(rectangle)
        self.cols = len(rectangle[0])

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for y in range(row1, row2 + 1):
            for x in range(col1, col2 + 1):
                self.rect[y][x] = newValue

    def getValue(self, row: int, col: int) -> int:
        if row >= self.rows or col >= self.cols:
            return -1
        return self.rect[row][col]

