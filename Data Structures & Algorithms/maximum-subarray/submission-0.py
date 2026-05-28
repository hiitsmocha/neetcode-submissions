class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # One pass Kadane Algo
        maxSum = nums[0]
        curSum = 0

        for i in nums:
            # if the current subarray sum is negative then we discard it
            # equivalent of saying we set it to 0
            curSum = max(curSum, 0)
            curSum += i # here we update the current sum, to prepare it for the next iteration
            maxSum = max(maxSum, curSum) # if the curSum is positive then we set it to max, else leave it
        return maxSum