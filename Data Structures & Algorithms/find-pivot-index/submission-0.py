class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # accumulate the prefix sums array
        total = 0
        prefix_arr = []
        for i in range(len(nums)):
            total += nums[i]
            prefix_arr.append(total)
        for i in range(len(nums)):
            if prefix_arr[0] == prefix_arr[len(nums) - 1]:
                return 0
            elif i == len(nums)-1:
                return -1
            elif prefix_arr[len(nums) - 1] == prefix_arr[i] + prefix_arr[i+1]:
                return (i+1)
        return -1
            
            
