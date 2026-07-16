class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            arr = [0] * 26
            for j in i:
                arr[ord(j) - ord("a")] += 1
            if tuple(arr) in hashmap:
                hashmap[tuple(arr)].append(i)
            else:
                hashmap[tuple(arr)] = [i]
        return list(hashmap.values())

            