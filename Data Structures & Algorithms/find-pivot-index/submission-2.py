class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # approach 1: half of the sum
        # excluding the item itself
        left_sum = 0
        total_sum = 0
        for i in nums:
            total_sum += i
        print(total_sum)
        for i in range(len(nums)):
            if left_sum * 2 == (total_sum - nums[i]):
                return i
            left_sum += nums[i]
        return -1