class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        map = {}

        for num in nums2:
            while stack and stack[-1] < num:
                map[stack.pop()] = num
            stack.append(num)
        return [map.get(num, -1) for num in nums1]