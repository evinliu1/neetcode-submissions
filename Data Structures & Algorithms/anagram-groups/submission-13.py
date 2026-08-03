class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashmap = defaultdict(list)

        for word in strs:
            hash = [0] * 26
            for char in word:
                hash[ord(char) - ord('a')] += 1
            hashmap[tuple(hash)].append(word)
        for val in hashmap.values():
            res.append(val)
        return res