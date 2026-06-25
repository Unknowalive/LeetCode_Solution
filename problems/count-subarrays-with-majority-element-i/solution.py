class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + (1 if nums[i] == target else 0)
        
        result = 0
        for i in range(n):
            for j in range(i, n):
                length = j - i + 1
                count_target = prefix[j+1] - prefix[i]
                if count_target > length // 2:
                    result += 1
        return result
