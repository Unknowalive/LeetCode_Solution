class Solution {
    public int uniquePaths(int m, int n) {
        int N = m + n - 2;
        int K = Math.min(m - 1, n - 1);
        long res = 1;
        for (int i = 1; i <= K; i++) {
            res = res * (N - i + 1) / i;
        }
        return (int) res;
    }
}