class Solution(object):
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7
        m = r - l + 1
        if n == 1:
            return m % MOD
        if n == 2:
            return (m * (m - 1)) % MOD
        def matmul(A, B):
            C = [[0] * m for _ in range(m)]
            for i in range(m):
                for k in range(m):
                    if A[i][k]:
                        for j in range(m):
                            C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C
        def vec_mul(A, v):
            res = [0] * m
            for i in range(m):
                for j in range(m):
                    if A[i][j]:
                        res[i] = (res[i] + A[i][j] * v[j]) % MOD
            return res
        M = [[0] * m for _ in range(m)]
        for v in range(m):
            for u in range(m - v, m):
                M[v][u] = 1

        power = n - 2
        V = [i for i in range(m)]
        res_M = [[1 if i == j else 0 for j in range(m)] for i in range(m)]
        base_M = M

        while power > 0:
            if power & 1:
                res_M = matmul(res_M, base_M)
            base_M = matmul(base_M, base_M)
            power >>= 1

        final_V = vec_mul(res_M, V)
        return (2 * sum(final_V)) % MOD