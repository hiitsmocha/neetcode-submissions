class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        hashmap1 = {}

        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 1

        for i in range(len(t)):
            if t[i] in hashmap1:
                hashmap1[t[i]] += 1
            else:
                hashmap1[t[i]] = 1

        return hashmap1 == hashmap