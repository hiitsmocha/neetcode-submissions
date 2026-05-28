class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        running_counter = 0
        highest_counter = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                running_counter += 1
            else:
                highest_counter = max(running_counter, highest_counter)
                running_counter = 0
        highest_counter = max(running_counter, highest_counter)
        return highest_counter