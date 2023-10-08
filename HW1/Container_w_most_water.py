class Solution:
    def maxArea(self, height: List[int]) -> int:
        vol = 0
        l = 0
        r = len(height) - 1
        while l < r:
            v = min(height[l], height[r])*(r - l)
            vol = max(vol, v)
            # print(vol)
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return vol 

