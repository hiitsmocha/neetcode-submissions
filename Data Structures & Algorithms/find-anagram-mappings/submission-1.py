class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        for i in range(len(nums2)):
            hashmap[nums2[i]] = i
        return_arr = []
        for i in range(len(nums1)):
            return_arr.append(hashmap[nums1[i]])
        return return_arr