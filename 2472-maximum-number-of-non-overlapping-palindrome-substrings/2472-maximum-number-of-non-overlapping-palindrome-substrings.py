class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        count = 0
        i = 0
        
        while i <= n - k:
            # Check for palindromes starting at or after index i
            # We only care about the first one we hit to keep it greedy
            found = False
            
            # Check every possible center for a palindrome of length k or k+1
            # within a small window starting at i
            for j in range(i, i + k):
                if found: break
                
                # Check for two types of centers:
                # 1. Single character center (odd length)
                # 2. Between two characters (even length)
                for l, r in [(j, j), (j, j + 1)]:
                    while l >= i and r < n and s[l] == s[r]:
                        if r - l + 1 >= k:
                            count += 1
                            i = r + 1 # Jump past this palindrome
                            found = True
                            break
                        l -= 1
                        r += 1
                    if found: break
            
            if not found:
                i += 1
                
        return count