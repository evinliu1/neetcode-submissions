class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        keys = defaultdict(list)
        res = []
        for string in strs:
            shash = [0] * 26
            for char in string:
                shash[ord(char) - ord('a')] += 1
            # now we have hash of each string
            keys[tuple(shash)].append(string)
        return list(keys.values())