class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        int[] counts = new int[26];
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();
        
        for (int i = 0; i < sArr.length; i++) {
            counts[sArr[i] - 'a']++;
            counts[tArr[i] - 'a']--;
        }
        
        for (int count : counts) {
            if (count != 0) {
                return false;
            }
        }
        
        return true;
    }
}