class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = []
        suffix_arr = []
        total_left = 1
        total_right = 1
        # prefix array -- exclude the current number --> append first then update
        for i in nums:
            prefix_arr.append(total_left)
            total_left *= i
        # suffix array
        for i in range(len(nums) - 1, -1, -1):
            suffix_arr.append(total_right)
            total_right *= nums[i]
        # last step
        return_arr = []
        for i in range(len(nums)):
            return_arr.append(prefix_arr[i] * suffix_arr[len(nums) - 1 - i])
        return return_arr