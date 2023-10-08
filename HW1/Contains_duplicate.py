class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in nums:
            hashmap[i] = 1+hashmap.get(i,0)
            if hashmap[i] > 1:
                return True
        return False
