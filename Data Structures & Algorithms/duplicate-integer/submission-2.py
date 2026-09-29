class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        thisdict = dict();
        for num in nums:
            if num in thisdict:
                return True;
            thisdict[num] = 1;
        return False;