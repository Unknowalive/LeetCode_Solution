class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        
        // 1. Place each number in its correct position: nums[i] should equal i + 1
        for (int i = 0; i < n; i++) {
            while (nums[i] > 0 && nums[i] <= n && nums[nums[i] - 1] != nums[i]) {
                // Swap nums[i] with the element at its target position (nums[i] - 1)
                int correctIndex = nums[i] - 1;
                int temp = nums[i];
                nums[i] = nums[correctIndex];
                nums[correctIndex] = temp;
            }
        }
        
        // 2. Find the first index where nums[i] != i + 1
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }
        
        // 3. If all numbers from 1 to n are present, the answer is n + 1
        return n + 1;
    }
}