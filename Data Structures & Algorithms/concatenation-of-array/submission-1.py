class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # actual concatenation
        # creating an array of 2x size
        newArr = [0]*(2*len(nums))
        for i, num in enumerate(nums):
            newArr[i] = newArr[i+len(nums)] = num
        return newArr
