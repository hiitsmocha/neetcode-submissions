class Solution:
    def countElements(self, arr: List[int]) -> int:
        total_elem = 0
        hashmap = {}
        for i in range(len(arr)):
            if arr[i] in hashmap:
                hashmap[arr[i]] += 1
            else:
                hashmap[arr[i]] = 1
        print(hashmap)
        for i in set(arr):
            if i + 1 in hashmap:
                total_elem += hashmap[i]
        return total_elem