class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        max_val = max(nums)
        points = [0] * (max_val + 1)
        for num in nums:
            points[num] += num
            
        prev2, prev1 = 0, 0
        
        for val in points:
            current = max(prev1, prev2 + val)
            prev2 = prev1
            prev1 = current
            
        return prev1