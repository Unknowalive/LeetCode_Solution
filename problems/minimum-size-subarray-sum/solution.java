class Solution {
    public int minSubArrayLen(int target, int[] nums) {
     int left = 0;
        int currentSum = 0;
        int minLen = 1000001;

        for (int right = 0; right < nums.length; right++) {
            currentSum += nums[right];   
   while (currentSum >= target) {
                minLen = Math.min(minLen, right - left + 1);
                currentSum -= nums[left];
                left++;
            }
        }
        return minLen == 1000001 ? 0 : minLen;
    }
}