class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        st = set()
        for i in range(len(nums)):
            target = -nums[i]
            hashmap = {}
            for j in range(i+1, len(nums)):
                if (target - nums[j]) in hashmap:
                    st.add(tuple(sorted([nums[i], nums[j], nums[hashmap[target-nums[j]]]])))
                hashmap[nums[j]] = j
        return list(st)