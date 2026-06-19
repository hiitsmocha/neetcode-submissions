class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return_arr = []
        for i in nums1:
            return_arr.append(nums2.index(i))
        return return_arr