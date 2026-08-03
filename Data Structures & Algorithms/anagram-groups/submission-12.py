class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for string in strs:
            hashmap = [0] * 26
            for char in string:
                hashmap[ord(char) - ord('a')] += 1
            count[tuple(hashmap)].append(string)
        return list(count.values())
