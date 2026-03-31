class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""

        for s in strs:
            ret += str(len(s))
            ret += '#'
            ret += s
        
        return ret
    
    def decode(self, s: str) -> List[str]:
        index = 0
        ret = []
        
        while index < len(s):
            lt = 0
            while s[index] != '#':
                lt *= 10
                lt += ord(s[index]) - ord('0')
                index += 1
            
            index += 1 # Skip over '#'

            build = ""
            for i in range(lt):
                build += s[index]
                index += 1
                

            ret.append(build)
        
        return ret
        