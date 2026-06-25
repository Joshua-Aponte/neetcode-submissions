class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        thisdict = dict()
        for string in strs:
            key = "".join(sorted(string))
            
            if key in thisdict:
                thisdict.get(key).append(string)
            else:
                myList = [string]
                thisdict[key] = myList
        return list(thisdict.values())