class Solution(object):
    def countPalindromePaths(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append((i, s[i]))
            
        # count_map stores {mask: frequency}
        count_map = {0: 1}
        self.ans = 0
        
        def dfs(u, current_mask):
            for v, char in adj[u]:
                # Update mask for the edge (u, v)
                char_bit = 1 << (ord(char) - ord('a'))
                new_mask = current_mask ^ char_bit
                
                # Case 1: All characters on path appear even times (mask ^ target = 0)
                self.ans += count_map.get(new_mask, 0)
                
                # Case 2: Exactly one character appears odd times (mask ^ target = 2^k)
                for i in range(26):
                    target_mask = new_mask ^ (1 << i)
                    self.ans += count_map.get(target_mask, 0)
                
                # Update the map and continue DFS
                count_map[new_mask] = count_map.get(new_mask, 0) + 1
                dfs(v, new_mask)
        
        dfs(0, 0)
        return self.ans