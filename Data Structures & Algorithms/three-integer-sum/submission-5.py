class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            target = -nums[i]
            hashmap = {}
            for j in range(i + 1, len(nums)):
                if target - nums[j] in hashmap:
                    result.append(tuple(sorted([nums[i], nums[j], nums[hashmap[target - nums[j]]]])))
                else:
                    hashmap[nums[j]] = j
        return list(set(result))
            