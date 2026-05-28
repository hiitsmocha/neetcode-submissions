class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        hashmap1 = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 0
            hashmap[s[i]] += 1
            if t[i] not in hashmap1:
                hashmap1[t[i]] = 0
            hashmap1[t[i]] += 1
        return hashmap1 == hashmap