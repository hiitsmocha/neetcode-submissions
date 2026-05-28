class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # we try to build a prefix sum array for each of the rows
        self.prefix_sum_arr = []
        for i in range(len(matrix)):
            prefix_sum = 0
            prefix_sum_row = []
            for j in range(len(matrix[i])):
                prefix_sum += matrix[i][j]
                prefix_sum_row.append(prefix_sum)
            self.prefix_sum_arr.append(prefix_sum_row)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # query the prefix_sum_arr (a matrix)
        # result by row
        total_sum = 0
        for row in range(row1, row2 + 1):
            right_sum = self.prefix_sum_arr[row][col2]
            left_sum = self.prefix_sum_arr[row][col1 - 1] if col1 > 0 else 0
            total_sum += right_sum - left_sum
        return total_sum



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)