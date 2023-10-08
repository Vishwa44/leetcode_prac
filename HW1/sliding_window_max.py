from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxlist = []
        p_q = deque(maxlen=k)
        for i,j in enumerate(nums):
            while len(p_q) > 0 and p_q[-1][1] < j:
                p_q.pop()
            p_q.append([i,j])
            if i >= k-1:
                if p_q[0][0] < i-(k-1):
                    p_q.popleft()
                maxlist.append(p_q[0][1])
        return maxlist
