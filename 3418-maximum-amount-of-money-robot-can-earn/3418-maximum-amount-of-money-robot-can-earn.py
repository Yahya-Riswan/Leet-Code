class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        m, n = len(coins), len(coins[0])
        # dp[i][j][k] represents max coins at (i, j) with k neutralizations REMAINING
        # Initializing with -float('inf') because coins can be negative
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]

        # Base case at (0, 0)
        val = coins[0][0]
        if val >= 0:
            dp[0][0][0] = dp[0][0][1] = dp[0][0][2] = val
        else:
            dp[0][0][2] = val # No neutralization used
            dp[0][0][1] = 0   # 1 neutralization used
            dp[0][0][0] = 0   # 2 used (effectively same as 1 here)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                val = coins[i][j]
                for k in range(3):
                    # Coming from Top or Left
                    prev_max = -float('inf')
                    if i > 0: prev_max = max(prev_max, dp[i-1][j][k])
                    if j > 0: prev_max = max(prev_max, dp[i][j-1][k])
                    
                    if prev_max == -float('inf'): continue

                    # Case 1: Don't use neutralization (or cell is positive)
                    dp[i][j][k] = max(dp[i][j][k], prev_max + val)

                    # Case 2: Use neutralization (only if k > 0 and val < 0)
                    if k > 0 and val < 0:
                        dp[i][j][k-1] = max(dp[i][j][k-1], prev_max)

        # Result is the max of having 0, 1, or 2 neutralizations left at the end
        return max(dp[m-1][n-1])