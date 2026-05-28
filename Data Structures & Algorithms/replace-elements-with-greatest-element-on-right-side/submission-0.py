class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 2, 0, -1):
            arr[i] = max(arr[i+1], arr[i]) 
        # shift left
        for i in range(1, len(arr)):
            arr[i-1] = arr[i]
        arr[-1] = -1
        return arr
            