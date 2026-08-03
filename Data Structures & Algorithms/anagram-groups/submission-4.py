class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        """
        Input: strs = ["act","pots","tops","cat","stop","hat"]
        Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
        """

        for s in strs:
            count = [0] * 26 # a b c .... z
            # [ 0 0 0 0 0 0 0 ] we will use this as the key
            # this resets each time for a new string in strings
            for c in s:
                # for each character in str
                count[ord(c) - ord('a')] += 1
                # this is how we increment the values in key
                # [ 0 0 1 0 1 0 0 1 ... ]
                # now we have the key for our word
                # it's time to add the key and str to the dict
                # key for "dog" is stored in variable "count"
            result[tuple(count)].append(s)
        return list(result.values())
        # return list form of only the values of the dict
        """
        result = {
            [ 0 0 0 ...] : ["dog", "god" ]
            [ 0 0 0 ...] : ["abc"]
        }
        """

        # returning result.values -> return ["dog", "god"], ["abc"]
        # returning list(result.values) ->
        # [["dog", "god"], ["abc"]]


                

        