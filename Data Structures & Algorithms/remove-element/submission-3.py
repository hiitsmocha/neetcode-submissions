class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        idx = 0
        while idx < n:
            if nums[idx] == val:
                for j in range(idx, n-1):
                    nums[j] = nums[j+1]
                n -= 1
            else:
                idx += 1
        return n