class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force double loop
        # this accounts for duplicate words but it's too inefficient
        # res = []
        # for i in range(len(strs)):
        #     char_ct = {}
        #     word = strs[i]
        #     matches = [word]
        #     for ch in word:
        #         char_ct[ch] = char_ct.get(ch, 0) + 1
        #     for j in range(len(strs)):
        #         if i == j:
        #             continue
        #         j_word = strs[j]
        #         j_ct = {}
        #         for ch in j_word:
        #             j_ct[ch] = j_ct.get(ch, 0) + 1

        #         if j_ct == char_ct:
        #             matches.append(j_word)
        #     if sorted(matches) in res:
        #         continue
        #     res.append(sorted(matches))
        # return res

        # more efficient approach - one pass
        # create a hash of each word

        res = defaultdict(list)
        for word in strs:
            char_hash = [0] * 26
            for ch in word:
                char_hash[ord(ch) - ord('a')] += 1
            res[tuple(char_hash)].append(word)
        
        return list(res.values())