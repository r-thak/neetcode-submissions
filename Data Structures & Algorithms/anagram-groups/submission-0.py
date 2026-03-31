class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        ret = []

        counter = 0
        for strih in strs:
            key = frozenset(Counter(strih).items())
            if not key in groups:
                groups.update({key:counter})
                counter += 1
                ret.append([strih])
            else:
                ret[groups[key]].append(strih)

        return ret
            
            
        