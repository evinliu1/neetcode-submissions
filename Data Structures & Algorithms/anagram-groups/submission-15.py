class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_to_word = defaultdict(list)
        for word in strs:
            hash = [0] * 26
            for char in word:
                hash[(ord(char) - ord('a'))] += 1
            hash_to_word[tuple(hash)].append(word)
        return list(hash_to_word.values())