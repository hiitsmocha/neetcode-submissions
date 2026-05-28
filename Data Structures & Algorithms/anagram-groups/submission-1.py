class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def anagram_hashmap(word):
            hashmap = {}
            for i in range(len(word)):
                if word[i] not in hashmap:
                    hashmap[word[i]] = 1
                else:
                    hashmap[word[i]] += 1
            return hashmap
        
        outer_hashmap = {}
        for i in range(len(strs)):
            word_hashmap = anagram_hashmap(strs[i])
            key = tuple(sorted(word_hashmap.items()))
            if key in outer_hashmap:
                outer_hashmap[key].append(strs[i])
            else:
                outer_hashmap[key] = [strs[i]]
        return list(outer_hashmap.values())
