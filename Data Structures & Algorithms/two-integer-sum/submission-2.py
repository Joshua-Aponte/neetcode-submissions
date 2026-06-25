class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        thisdict = dict()
        i = 0
        current = 0
        supp = 0

        for num in nums:
            current = nums[i]
            supp = target - current
            if supp in thisdict:
                if thisdict[supp] < i:
                    return [thisdict[supp], i]
                else:
                    return [i, thisdict[supp]]
            thisdict[current] = i
            i += 1