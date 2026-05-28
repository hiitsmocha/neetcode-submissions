class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # idea: build a prefix product array and a postfix product array 
        # take product
        prefix_arr, postfix_arr = [], []
        prefix, postfix = 1, 1
        for i in range(len(nums)):
            if i > 0:
                prefix *= nums[i - 1]
            prefix_arr.append(prefix)
        for j in range(len(nums) - 1, -1, - 1):
            if j < len(nums) - 1:
                postfix *= nums[j + 1]
            postfix_arr.append(postfix)
        print(prefix_arr)
        print(postfix_arr)
        for k in range(len(nums)):
            prefix_arr[k] *= postfix_arr[len(nums) - k - 1]
        return prefix_arr

