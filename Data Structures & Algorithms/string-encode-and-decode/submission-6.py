class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += str(len(word)) + "#" + word
        return string 



    def decode(self, s: str) -> List[str]:
        string = s
        i, solution = 0, []
        while i < len(string):
            pointer = i
            while string[pointer] != "#":
                pointer += 1
            length = int(string[i:pointer])
            solution.append(string[pointer + 1: pointer + 1 + length])
            i = pointer + 1 + length
        return solution
            
        