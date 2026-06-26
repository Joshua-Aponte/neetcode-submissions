class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = Counter(nums).most_common(k)
        thislist = [item[0] for item in counted]
        return thislist

        
        
            