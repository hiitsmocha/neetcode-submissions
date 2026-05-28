class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_arr = []
        for i in range(len(matrix)):
            self.inner_prefix_arr = []
            total = 0
            for j in range(len(matrix[i])):
                total += matrix[i][j]
                self.inner_prefix_arr.append(total)
            self.prefix_arr.append(self.inner_prefix_arr)

    def rangeSum(self, arr: List, left: int, right: int) -> int:
        preRight = arr[right]
        preLeft = arr[left - 1] if left > 0 else 0
        return (preRight - preLeft)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2 + 1):
            total += self.rangeSum(self.prefix_arr[i], col1, col2)
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)