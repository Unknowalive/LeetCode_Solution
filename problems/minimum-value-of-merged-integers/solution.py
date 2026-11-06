class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        min_val = float('inf')
        for i in range(0, len(nums), 2):
            merged = int(str(nums[i]) + str(nums[i+1]))
            if merged < min_val:
                min_val = merged
        return min_val
