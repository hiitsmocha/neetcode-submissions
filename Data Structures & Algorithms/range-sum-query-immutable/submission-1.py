class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        self.current_sum = 0
        for i in range(len(nums)):
            self.prefix_sum.append(nums[i] + self.current_sum)
            self.current_sum += nums[i]

    def sumRange(self, left: int, right: int) -> int:
        right_prefix = self.prefix_sum[right]
        left_prefix = self.prefix_sum[left-1] if left > 0 else 0
        return right_prefix - left_prefix


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)