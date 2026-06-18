class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        sorted_set = set("".join(sorted(i)) for i in strs)
        for i in sorted_set:
            hashmap[i] = []
        for i in range(len(strs)):
            hashmap["".join(sorted(strs[i]))].append(strs[i])
        return list(hashmap.values())
            