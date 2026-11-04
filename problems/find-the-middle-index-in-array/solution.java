class Solution {
    public int findMiddleIndex(int[] nums) {
        int totalSum = 0;
        int len = nums.length;
        
        // Use indexed loops for faster execution in Java
        for (int i = 0; i < len; i++) {
            totalSum += nums[i];
        }
        
        int leftSum = 0;
        for (int i = 0; i < len; i++) {
            // Avoid re-calculating right sum inside the loop directly
            if (leftSum == totalSum - leftSum - nums[i]) {
                return i;
            }
            leftSum += nums[i];
        }
        
        return -1;
    }
}