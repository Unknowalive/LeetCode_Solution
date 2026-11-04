class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();
        if (s == null || s.length() == 0 || words == null || words.length == 0) {
            return result;
        }

        int wordLen = words[0].length();
        int numWords = words.length;
        int totalLen = wordLen * numWords;
        int sLen = s.length();

        if (sLen < totalLen) {
            return result;
        }

        // 1. Build frequency map for expected words
        Map<String, Integer> wordMap = new HashMap<>();
        for (String w : words) {
            wordMap.put(w, wordMap.getOrDefault(w, 0) + 1);
        }

        // 2. Try all possible starting offsets (0 to wordLen - 1)
        for (int i = 0; i < wordLen; i++) {
            Map<String, Integer> currentMap = new HashMap<>();
            int left = i;
            int count = 0; // Number of valid words matched in current window

            // Move the right pointer by step size of wordLen
            for (int right = i; right + wordLen <= sLen; right += wordLen) {
                String word = s.substring(right, right + wordLen);

                if (wordMap.containsKey(word)) {
                    currentMap.put(word, currentMap.getOrDefault(word, 0) + 1);
                    count++;

                    // If word frequency exceeds what's required, shrink window from left
                    while (currentMap.get(word) > wordMap.get(word)) {
                        String leftWord = s.substring(left, left + wordLen);
                        currentMap.put(leftWord, currentMap.get(leftWord) - 1);
                        count--;
                        left += wordLen;
                    }

                    // If all words are matched, add left starting index
                    if (count == numWords) {
                        result.add(left);
                    }
                } else {
                    // Invalid word: reset window
                    currentMap.clear();
                    count = 0;
                    left = right + wordLen;
                }
            }
        }

        return result;
    }
}