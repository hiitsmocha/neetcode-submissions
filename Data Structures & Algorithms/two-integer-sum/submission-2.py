class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}        
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in hashmap and hashmap[ans] != i:
                return[hashmap[ans], i]
            hashmap[nums[i]] = i
        return []