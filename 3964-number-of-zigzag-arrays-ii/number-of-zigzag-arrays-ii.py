class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        
        MOD = 10**9 + 7
        M = r - l + 1
        
        # 1. Helper function for matrix multiplication under modulo
        def mat_mul(A, B):
            size = len(A)
            result = [[0] * size for _ in range(size)]
            for i in range(size):
                for k in range(size):
                    if A[i][k] == 0:
                        continue
                    for j in range(size):
                        result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
            return result

        # 2. Helper function for fast matrix exponentiation
        def mat_pow(matrix, power):
            size = len(matrix)
            result = [[0] * size for _ in range(size)]
            for i in range(size):
                result[i][i] = 1  # Identity matrix
                
            base = matrix
            while power > 0:
                if power % 2 == 1:
                    result = mat_mul(result, base)
                base = mat_mul(base, base)
                power //= 2
            return result

        # 3. Build the core transition matrix T
        # T[i][j] represents transition from element i to element j (using 0-indexed values)
        # By setting up T for a specific direction constraint, we leverage symmetry later.
        T = [[0] * M for _ in range(M)]
        for i in range(M):
            for j in range(M):
                if i + j >= M:
                    T[i][j] = 1

        # 4. Compute T^(n-1)
        final_T = mat_pow(T, n - 1)

        # 5. Sum all valid paths
        # Multiply by 2 to account for both starting direction trends (up-down vs down-up)
        total_ways = 0
        for i in range(M):
            for j in range(M):
                total_ways = (total_ways + final_T[i][j]) % MOD
                
        return (total_ways * 2) % MOD
